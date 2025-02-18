from django.db import models



class BookNews(models.Model):
    title = models.CharField('Название книги', max_length=100)
    author = models.CharField('Имя автора', max_length=150)
    isbn = models.CharField('Серия', max_length=50, unique=True)
    edition = models.CharField('Версия', max_length=50)
    publisher = models.CharField('Издатель', max_length=110)
    description = models.TextField('Описание')
    image = models.ImageField('Фото книги', upload_to='books/')
    pages = models.IntegerField('Количество страниц', blank=True, null=True)
    book_format = models.CharField('Формат книги', max_length=50)
    is_active = models.BooleanField('Доступность', default=True)
    genres = models.ManyToManyField(Genre, related_name='book_genre')
    tags = models.ManyToManyField(Tag, related_name='book_tag')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
















