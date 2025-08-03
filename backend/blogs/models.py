from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
import markdown
import re

User = get_user_model()


class Category(models.Model):
    """Blog category model."""
    
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Auto-generate slug if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    """Blog tag model."""
    
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Auto-generate slug if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Blog(models.Model):
    """Blog post model."""
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(
        max_length=200,
        help_text='Enter the title of your blog post'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text='URL-friendly version of the title'
    )
    content = models.TextField(
        help_text='Write your blog content here'
    )
    excerpt = models.TextField(
        max_length=500,
        blank=True,
        help_text='A brief summary of your blog post (optional)'
    )
    featured_image = models.ImageField(
        upload_to='blog_images/',
        blank=True,
        null=True,
        help_text='Featured image for your blog post (optional)'
    )
    
    # Relationships
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blogs',
        help_text='The author of this blog post'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='blogs',
        help_text='Category for this blog post (optional)'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='blogs',
        help_text='Tags for this blog post (optional)'
    )
    
    # Status and visibility
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='published',
        help_text='Publication status of the blog post'
    )
    is_featured = models.BooleanField(
        default=False,
        help_text='Mark this post as featured'
    )
    
    # SEO and metadata
    meta_title = models.CharField(
        max_length=60,
        blank=True,
        help_text='SEO title (optional, defaults to post title)'
    )
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        help_text='SEO description (optional, defaults to excerpt)'
    )
    
    # Analytics
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status', 'created_at']),
            models.Index(fields=['author', 'status']),
            models.Index(fields=['category', 'status']),
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """Auto-generate slug and excerpt if not provided."""
        if not self.slug:
            self.slug = slugify(self.title)
        
        if not self.excerpt and self.content:
            # Create excerpt from content (first 150 characters)
            plain_text = re.sub(r'<[^>]+>', '', self.content)
            self.excerpt = plain_text[:150] + '...' if len(plain_text) > 150 else plain_text
        
        # Set published_at when status changes to published
        if self.status == 'published' and not self.published_at:
            from django.utils import timezone
            self.published_at = timezone.now()
        
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        """Get the absolute URL for this blog post."""
        return reverse('blog_detail', kwargs={'slug': self.slug})
    
    @property
    def reading_time(self):
        """Calculate estimated reading time in minutes."""
        word_count = len(self.content.split())
        return max(1, round(word_count / 200))  # Average reading speed: 200 words/minute
    
    @property
    def word_count(self):
        """Get the word count of the content."""
        return len(self.content.split())
    
    @property
    def formatted_content(self):
        """Convert markdown content to HTML."""
        return markdown.markdown(self.content, extensions=['extra', 'codehilite'])
    
    def increment_views(self):
        """Increment the view count."""
        self.views += 1
        self.save(update_fields=['views'])
    
    def increment_likes(self):
        """Increment the like count."""
        self.likes += 1
        self.save(update_fields=['likes'])
    
    def get_meta_title(self):
        """Get the meta title, fallback to post title."""
        return self.meta_title or self.title
    
    def get_meta_description(self):
        """Get the meta description, fallback to excerpt."""
        return self.meta_description or self.excerpt


class Comment(models.Model):
    """Blog comment model."""
    
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    content = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Comment by {self.author.name} on {self.blog.title}'
    
    @property
    def is_reply(self):
        """Check if this comment is a reply to another comment."""
        return self.parent is not None 