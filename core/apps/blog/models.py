from django.db import models

# Create your models here.
#
# class Post(models.Model):
#     title = models.CharField('Название поста', max_length=100)
#     text = models.TextField('Text')
#     image = models.ImageField('Фото поста', upload_to='posts')
#     created_at = models.DateTimeField('Дата создания', auto_now_add=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_post')
#     tags = models.ManyToManyField(Tag, related_name='tag_post')
#     # author =
