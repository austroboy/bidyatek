from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'author', 'published_date', 'is_published']
    list_filter = ['is_published', 'author']
    search_fields = ['title_en', 'content_en']
    prepopulated_fields = {'slug': ('title_en',)}
    date_hierarchy = 'published_date'