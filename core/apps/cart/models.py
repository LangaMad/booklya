from django.db import models
from ..books.models import Book
# Create your models here.

class Cart(models.Model):
    books = models.ManyToManyField(Book, through='CartItem', related_name='cart_book')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='user_cart')
    total_price = models.DecimalField('Общая цена', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина пользователя'

    def calculate_total_price(self):
        total = 0
        for item in self.cart_item.all():
            total += item.book.price * item.quantity
        self.total_price = total
        self.save()  # Сохраняем корзину после вычисления общей цены
        return self.total_price



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_cart_item')
    quantity = models.PositiveIntegerField('Количество', default=1)

    def __str__(self):
        return f'Книга {self.book.title} в корзине '