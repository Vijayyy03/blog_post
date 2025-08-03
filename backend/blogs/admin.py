from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Blog, Category, Tag, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for Category model."""
    
    list_display = ['name', 'slug', 'blog_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
    
    def blog_count(self, obj):
        """Display the number of blogs in this category."""
        return obj.blogs.count()
    blog_count.short_description = 'Blog Count'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin interface for Tag model."""
    
    list_display = ['name', 'slug', 'blog_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at']
    
    def blog_count(self, obj):
        """Display the number of blogs with this tag."""
        return obj.blogs.count()
    blog_count.short_description = 'Blog Count'


class CommentInline(admin.TabularInline):
    """Inline admin for comments."""
    
    model = Comment
    extra = 0
    readonly_fields = ['created_at', 'updated_at']
    fields = ['author', 'content', 'is_approved', 'created_at']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Admin interface for Blog model."""
    
    list_display = [
        'title', 'author', 'category', 'status', 'is_featured',
        'views', 'likes', 'reading_time', 'created_at', 'featured_image_display'
    ]
    list_filter = [
        'status', 'is_featured', 'category', 'tags', 'created_at',
        'published_at', 'author'
    ]
    search_fields = ['title', 'content', 'excerpt', 'author__name']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = [
        'views', 'likes', 'reading_time', 'word_count', 'created_at',
        'updated_at', 'published_at', 'formatted_content_display'
    ]
    filter_horizontal = ['tags']
    inlines = [CommentInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'content', 'excerpt', 'featured_image')
        }),
        ('Relationships', {
            'fields': ('author', 'category', 'tags')
        }),
        ('Status & Visibility', {
            'fields': ('status', 'is_featured')
        }),
        ('SEO & Metadata', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Analytics', {
            'fields': ('views', 'likes', 'reading_time', 'word_count'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'published_at'),
            'classes': ('collapse',)
        }),
        ('Formatted Content', {
            'fields': ('formatted_content_display',),
            'classes': ('collapse',)
        }),
    )
    
    def featured_image_display(self, obj):
        """Display featured image in admin list."""
        if obj.featured_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover;" />',
                obj.featured_image.url
            )
        return 'No image'
    featured_image_display.short_description = 'Featured Image'
    
    def formatted_content_display(self, obj):
        """Display formatted content in admin."""
        if obj.content:
            return mark_safe(obj.formatted_content)
        return 'No content'
    formatted_content_display.short_description = 'Formatted Content'
    
    def save_model(self, request, obj, form, change):
        """Set author if creating new blog post."""
        if not change:  # Creating new blog post
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin interface for Comment model."""
    
    list_display = [
        'author', 'blog', 'content_preview', 'is_approved',
        'is_reply', 'created_at'
    ]
    list_filter = ['is_approved', 'created_at', 'blog__author']
    search_fields = ['content', 'author__name', 'blog__title']
    readonly_fields = ['created_at', 'updated_at']
    actions = ['approve_comments', 'disapprove_comments']
    
    fieldsets = (
        ('Comment Information', {
            'fields': ('blog', 'author', 'parent', 'content')
        }),
        ('Moderation', {
            'fields': ('is_approved',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def content_preview(self, obj):
        """Show content preview in admin list."""
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
    content_preview.short_description = 'Content Preview'
    
    def is_reply(self, obj):
        """Show if comment is a reply."""
        return obj.parent is not None
    is_reply.boolean = True
    is_reply.short_description = 'Is Reply'
    
    def approve_comments(self, request, queryset):
        """Approve selected comments."""
        updated = queryset.update(is_approved=True)
        self.message_user(request, f'{updated} comments were approved.')
    approve_comments.short_description = 'Approve selected comments'
    
    def disapprove_comments(self, request, queryset):
        """Disapprove selected comments."""
        updated = queryset.update(is_approved=False)
        self.message_user(request, f'{updated} comments were disapproved.')
    disapprove_comments.short_description = 'Disapprove selected comments' 