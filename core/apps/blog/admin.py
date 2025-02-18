from django.contrib import admin
from .models import Post, PostCategory, PostCommentary


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'text',
        'image',
        'created_at',
        'author',
        'category'
    ]
    list_filter = ['created_at', 'category']
    search_fields = ['author__username', 'title']
    filter_horizontal = ('tags',)

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    display_tags.short_description = 'Теги'


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(PostCommentary)
class PostCommentaryAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'comment_text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'post__title']
