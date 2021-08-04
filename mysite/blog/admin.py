from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'author', 'created','status')
    list_filter = ('author','status')
    repopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active',)
    list_filter = ('active', 'created', 'updated',)
    search_fields = ('name', 'email', 'body')