from django.contrib import admin
from .models import BookNews


@admin.register(BookNews)
class BookNewsAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'author',
        'description',
        'image',
        'price',
]
    search_fields = ['title', 'author']
    list_filter = ['author']
    ordering = ['-created_at']
    filter_horizontal = ('tags','category')

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Теги'


    def get_news_detail(self, obj):
        return obj.news_detail.title
    get_news_detail.short_description = 'Книги'


    def get_category(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_tags.short_description = 'Категории'

