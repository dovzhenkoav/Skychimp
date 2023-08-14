from django.contrib import admin

from app_blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'view_counter', 'publication_date')
    list_filter = ('view_counter',)
    search_fields = ('title', 'text')
