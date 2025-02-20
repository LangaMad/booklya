from django.db import models
from ..books.models import Book, Tag
from ..blog.models import PostCategory





class BookNews(models.Model):
    title = models.CharField('Название книги', max_length=100)
    author = models.CharField('Имя автора', max_length=150)
    description = models.TextField('Описание')
    image = models.ImageField('Фото книги', upload_to='books/')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='news_tag' )
    category = models.ManyToManyField(PostCategory, related_name='news_category')
    news_detail = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_news')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'





















