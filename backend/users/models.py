from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    """Custom user manager for email-based authentication."""
    
    def create_user(self, email, name, password=None, **extra_fields):
        """Create and save a regular user."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password=None, **extra_fields):
        """Create and save a superuser."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, name, password, **extra_fields)


class User(AbstractUser):
    """Custom User model for the blog application."""
    
    # Remove username field and use email as the primary identifier
    username = None
    
    email = models.EmailField(
        unique=True,
        verbose_name='Email address',
        help_text='Required. Enter a valid email address.'
    )
    
    name = models.CharField(
        max_length=100,
        verbose_name='Full name',
        help_text='Enter your full name.'
    )
    
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name='Profile picture',
        help_text='Upload a profile picture (optional).'
    )
    
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='Bio',
        help_text='Tell us about yourself (optional).'
    )
    
    website = models.URLField(
        blank=True,
        verbose_name='Website',
        help_text='Your personal website (optional).'
    )
    
    # Social media links
    twitter = models.URLField(
        blank=True,
        verbose_name='Twitter',
        help_text='Your Twitter profile URL (optional).'
    )
    
    linkedin = models.URLField(
        blank=True,
        verbose_name='LinkedIn',
        help_text='Your LinkedIn profile URL (optional).'
    )
    
    github = models.URLField(
        blank=True,
        verbose_name='GitHub',
        help_text='Your GitHub profile URL (optional).'
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Use email as the username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    # Use custom manager
    objects = UserManager()
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        """Return the user's full name."""
        return self.name
    
    def get_short_name(self):
        """Return the user's short name."""
        return self.name.split()[0] if self.name else self.email
    
    @property
    def initials(self):
        """Return user's initials."""
        if self.name:
            names = self.name.split()
            if len(names) >= 2:
                return f"{names[0][0]}{names[-1][0]}".upper()
            return names[0][0].upper() 