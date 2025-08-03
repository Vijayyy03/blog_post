from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    UserBlogListView,
    MyBlogListView,
    CategoryListView,
    TagListView,
    CommentListView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    like_blog,
    featured_blogs,
    popular_blogs
)

urlpatterns = [
    # Blog CRUD endpoints
    path('', BlogListView.as_view(), name='blog-list'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    
    # Category and tag endpoints (must come before slug patterns)
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    
    # Special endpoints (must come before slug patterns)
    path('featured/', featured_blogs, name='featured-blogs'),
    path('popular/', popular_blogs, name='popular-blogs'),
    
    # User blog endpoints
    path('user/<int:user_id>/', UserBlogListView.as_view(), name='user-blogs'),
    path('my-blogs/', MyBlogListView.as_view(), name='my-blogs'),
    
    # Comment endpoints
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    
    # Blog detail and update endpoints (must come last)
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('<slug:slug>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path('<slug:slug>/like/', like_blog, name='like-blog'),
    
    # Comment endpoints for specific blogs
    path('<slug:blog_slug>/comments/', CommentListView.as_view(), name='comment-list'),
    path('<slug:blog_slug>/comments/create/', CommentCreateView.as_view(), name='comment-create'),
] 