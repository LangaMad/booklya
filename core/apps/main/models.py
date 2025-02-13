from django.db import models

# Create your models here.
class ContactUs(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.EmailField('Электронная почта', max_length=70)
    phone = models.CharField('Телефон', max_length=50)  # Corrected label
    text = models.TextField('Текст')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'