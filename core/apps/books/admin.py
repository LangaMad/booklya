from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display =['name']
    prepopulated_fields = {'slug':('name',)}



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'isbn',
        'rate',
        'edition',
        'publisher',
        'description',
        'image',
        'pages',
        'is_book',
        'is_active',
        'display_genres',
        'display_tags',
    ]
    list_filter = ['is_active',
                   'genres',
                   'tags']
    search_fields = ['title',
                     'author',
                     'isbn']
    filter_horizontal = ('tags', 'genres')

    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
    display_genres.short_description = "Жанры"

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    display_tags.short_description = "Теги"



@admin.register(BookLanguage)
class LanguageAdmin(admin.ModelAdmin):
    list_display = [
        'book',
        'language',
        'book_file'
    ]
    list_filter = ['language']
    search_fields = ['book__title', 'language']