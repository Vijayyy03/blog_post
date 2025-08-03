from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Custom admin interface for User model."""
    
    list_display = ('email', 'name', 'is_active', 'is_staff', 'date_joined', 'avatar_display')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'date_joined')
    search_fields = ('email', 'name')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': ('name', 'avatar', 'bio', 'website', 'twitter', 'linkedin', 'github')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    
    def avatar_display(self, obj):
        """Display avatar in admin list."""
        if obj.avatar:
            return format_html(
                '<img src="{}" width="30" height="30" style="border-radius: 50%;" />',
                obj.avatar.url
            )
        return format_html(
            '<div style="width: 30px; height: 30px; background-color: #e5e7eb; '
            'border-radius: 50%; display: flex; align-items: center; justify-content: center; '
            'font-weight: bold; color: #6b7280;">{}</div>',
            obj.initials
        )
    
    avatar_display.short_description = 'Avatar' 