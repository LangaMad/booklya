from django.db import models

# Create your models here.



class Genre(models.Model):
    name = models.CharField('Жанр', max_length=100, unique=True)
    slug = models.SlugField('Slug', max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'




class Tag(models.Model):
    name = models.CharField('Тег', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'



class Book(models.Model):
    title = models.CharField('Название книги', max_length=100)
    author = models.CharField('Имя автора', max_length=150)
    isbn = models.CharField('Серия', max_length=50, unique=True)
    rate = models.FloatField('Оценка')
    edition = models.CharField('Версия', max_length=50)
    publisher = models.CharField('Издатель', max_length=110)
    review = models.TextField('Отзыв')
    description = models.TextField('Описание')
    image = models.ImageField('Фото книги', upload_to='books/')
    pages = models.IntegerField('Количество страниц', blank=True, null=True)
    book_format = models.CharField('Формат книги', max_length=50)
    is_active = models.BooleanField('Доступность', default=True)
    genres = models.ManyToManyField(Genre, related_name='book_genre')
    tags = models.ManyToManyField(Tag, related_name='book_tag')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    comments = models.ManyToManyField('Commentary', blank=True, related_name='book_comments')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'



class BookLanguage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_languages')
    language = models.CharField('Язык', max_length=100, unique=False)
    book_file = models.FileField('Книга', upload_to='books/')

    def __str__(self):
        return f"{self.book} - {self.language}"

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

class AudioBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='audiobooks')
    language = models.CharField('Язык', max_length=100)
    audiobook_file = models.FileField('Аудиофайл', upload_to='audiobooks/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аудиокнига'
        verbose_name_plural = 'Аудиокниги'

class Commentary(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_comments')
    user_name = models.CharField('Имя пользователя', max_length=100)
    comment_text = models.TextField('Комментарий')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.user_name} на {self.book.title}"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'