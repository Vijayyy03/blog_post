from rest_framework import status, generics, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.db.models import Q, Count
from .models import Blog, Category, Tag, Comment
from .serializers import (
    BlogListSerializer,
    BlogDetailSerializer,
    BlogCreateSerializer,
    BlogUpdateSerializer,
    CategorySerializer,
    TagSerializer,
    CommentSerializer,
    CommentCreateSerializer
)
from .permissions import IsAuthorOrReadOnly, IsCommentAuthorOrReadOnly, IsAuthenticatedOrReadOnly


class BlogListView(generics.ListAPIView):
    """List all published blog posts with filtering and search."""
    
    serializer_class = BlogListSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'tags', 'author', 'status', 'is_featured']
    search_fields = ['title', 'content', 'excerpt', 'author__name']
    ordering_fields = ['created_at', 'updated_at', 'published_at', 'views', 'likes', 'title']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """Get queryset with optional filtering."""
        queryset = Blog.objects.filter(status='published').select_related(
            'author', 'category'
        ).prefetch_related('tags')
        
        # Filter by search query
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search) |
                Q(excerpt__icontains=search) |
                Q(author__name__icontains=search)
            )
        
        # Filter by tag
        tag = self.request.query_params.get('tag', None)
        if tag:
            queryset = queryset.filter(tags__name__icontains=tag)
        
        # Filter by category
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category__slug=category)
        
        # Filter by author
        author = self.request.query_params.get('author', None)
        if author:
            queryset = queryset.filter(author__id=author)
        
        return queryset.distinct()


class BlogDetailView(generics.RetrieveAPIView):
    """Retrieve a single blog post."""
    
    serializer_class = BlogDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
    def get_queryset(self):
        """Get queryset for published blogs."""
        return Blog.objects.filter(status='published').select_related(
            'author', 'category'
        ).prefetch_related('tags', 'comments__author')
    
    def retrieve(self, request, *args, **kwargs):
        """Retrieve blog and increment view count."""
        instance = self.get_object()
        instance.increment_views()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class BlogCreateView(generics.CreateAPIView):
    """Create a new blog post."""
    
    serializer_class = BlogCreateSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        """Create blog post with current user as author."""
        serializer.save(author=self.request.user)


class BlogUpdateView(generics.UpdateAPIView):
    """Update a blog post."""
    
    serializer_class = BlogUpdateSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = 'slug'
    
    def get_queryset(self):
        """Get queryset for user's blogs."""
        return Blog.objects.filter(author=self.request.user)


class BlogDeleteView(generics.DestroyAPIView):
    """Delete a blog post."""
    
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = 'slug'
    
    def get_queryset(self):
        """Get queryset for user's blogs."""
        return Blog.objects.filter(author=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        """Delete blog post."""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'message': 'Blog post deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)


class UserBlogListView(generics.ListAPIView):
    """List blog posts by a specific user."""
    
    serializer_class = BlogListSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        """Get queryset for user's published blogs."""
        user_id = self.kwargs.get('user_id')
        return Blog.objects.filter(
            author_id=user_id,
            status='published'
        ).select_related('author', 'category').prefetch_related('tags')


class MyBlogListView(generics.ListAPIView):
    """List current user's blog posts."""
    
    serializer_class = BlogListSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Get queryset for current user's blogs."""
        return Blog.objects.filter(author=self.request.user).select_related(
            'author', 'category'
        ).prefetch_related('tags')


class CategoryListView(generics.ListAPIView):
    """List all categories."""
    
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    queryset = Category.objects.annotate(blog_count=Count('blogs'))


class TagListView(generics.ListAPIView):
    """List all tags."""
    
    serializer_class = TagSerializer
    permission_classes = [AllowAny]
    queryset = Tag.objects.annotate(blog_count=Count('blogs'))


class CommentListView(generics.ListAPIView):
    """List comments for a blog post."""
    
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        """Get queryset for blog comments."""
        blog_slug = self.kwargs.get('blog_slug')
        blog = get_object_or_404(Blog, slug=blog_slug, status='published')
        return Comment.objects.filter(
            blog=blog,
            is_approved=True,
            parent=None  # Only top-level comments
        ).select_related('author').prefetch_related('replies__author')


class CommentCreateView(generics.CreateAPIView):
    """Create a new comment."""
    
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer_context(self):
        """Add blog to serializer context."""
        context = super().get_serializer_context()
        blog_slug = self.kwargs.get('blog_slug')
        context['blog'] = get_object_or_404(Blog, slug=blog_slug, status='published')
        return context


class CommentUpdateView(generics.UpdateAPIView):
    """Update a comment."""
    
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsCommentAuthorOrReadOnly]
    
    def get_queryset(self):
        """Get queryset for user's comments."""
        return Comment.objects.filter(author=self.request.user)


class CommentDeleteView(generics.DestroyAPIView):
    """Delete a comment."""
    
    permission_classes = [IsAuthenticated, IsCommentAuthorOrReadOnly]
    
    def get_queryset(self):
        """Get queryset for user's comments."""
        return Comment.objects.filter(author=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        """Delete comment."""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'message': 'Comment deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_blog(request, slug):
    """Like a blog post."""
    blog = get_object_or_404(Blog, slug=slug, status='published')
    blog.increment_likes()
    return Response({
        'message': 'Blog post liked successfully',
        'likes': blog.likes
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def featured_blogs(request):
    """Get featured blog posts."""
    blogs = Blog.objects.filter(
        status='published',
        is_featured=True
    ).select_related('author', 'category').prefetch_related('tags')[:6]
    
    serializer = BlogListSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def popular_blogs(request):
    """Get popular blog posts based on views."""
    blogs = Blog.objects.filter(
        status='published'
    ).select_related('author', 'category').prefetch_related('tags').order_by('-views')[:6]
    
    serializer = BlogListSerializer(blogs, many=True)
    return Response(serializer.data) 