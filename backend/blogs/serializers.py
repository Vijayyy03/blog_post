from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Blog, Category, Tag, Comment

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'created_at']


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag model."""
    
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model in blog context."""
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'avatar', 'bio', 'website']


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""
    
    author = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = [
            'id', 'content', 'author', 'parent', 'is_approved',
            'created_at', 'updated_at', 'replies'
        ]
        read_only_fields = ['author', 'is_approved', 'created_at', 'updated_at']
    
    def get_replies(self, obj):
        """Get replies for this comment."""
        replies = Comment.objects.filter(parent=obj, is_approved=True)
        return CommentSerializer(replies, many=True).data


class BlogListSerializer(serializers.ModelSerializer):
    """Serializer for blog list view."""
    
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'excerpt', 'featured_image',
            'author', 'category', 'tags', 'status', 'is_featured',
            'views', 'likes', 'reading_time', 'created_at', 'published_at'
        ]


class BlogDetailSerializer(serializers.ModelSerializer):
    """Serializer for blog detail view."""
    
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    formatted_content = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'content', 'formatted_content', 'excerpt',
            'featured_image', 'author', 'category', 'tags', 'status',
            'is_featured', 'views', 'likes', 'reading_time', 'word_count',
            'meta_title', 'meta_description', 'created_at', 'updated_at',
            'published_at', 'comments'
        ]
    
    def get_formatted_content(self, obj):
        """Get formatted HTML content."""
        return obj.formatted_content


class BlogCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating blog posts."""
    
    class Meta:
        model = Blog
        fields = [
            'title', 'content', 'excerpt', 'featured_image', 'category',
            'tags', 'status', 'is_featured', 'meta_title', 'meta_description'
        ]
    
    def create(self, validated_data):
        """Create a new blog post."""
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
    
    def validate_title(self, value):
        """Validate title field."""
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value.strip()
    
    def validate_content(self, value):
        """Validate content field."""
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Content must be at least 10 characters long.")
        return value.strip()
    
    def validate_excerpt(self, value):
        """Validate excerpt field."""
        if value and len(value) > 500:
            raise serializers.ValidationError("Excerpt cannot exceed 500 characters.")
        return value.strip() if value else value


class BlogUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating blog posts."""
    
    class Meta:
        model = Blog
        fields = [
            'title', 'content', 'excerpt', 'featured_image', 'category',
            'tags', 'status', 'is_featured', 'meta_title', 'meta_description'
        ]
    
    def validate_title(self, value):
        """Validate title field."""
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value.strip()
    
    def validate_content(self, value):
        """Validate content field."""
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Content must be at least 10 characters long.")
        return value.strip()
    
    def validate_excerpt(self, value):
        """Validate excerpt field."""
        if value and len(value) > 500:
            raise serializers.ValidationError("Excerpt cannot exceed 500 characters.")
        return value.strip() if value else value


class CommentCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating comments."""
    
    class Meta:
        model = Comment
        fields = ['content', 'parent']
    
    def create(self, validated_data):
        """Create a new comment."""
        validated_data['author'] = self.context['request'].user
        validated_data['blog'] = self.context['blog']
        return super().create(validated_data)
    
    def validate_content(self, value):
        """Validate comment content."""
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Comment must be at least 2 characters long.")
        return value.strip() 