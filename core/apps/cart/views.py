from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.generic import TemplateView
from .models import Cart, CartItem
from ..books.models import Book

class CartGenericView(TemplateView):
    template_name = 'pages/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        action = self.kwargs.get('action')
        cart_item_id = self.kwargs.get('cart_item_id')

        # Проверка, что пользователь аутентифицирован
        if not self.request.user.is_authenticated:
            return redirect('login')  # Перенаправление на страницу входа

        cart = Cart.objects.filter(user=self.request.user).first()

        if action == 'add':
            book = get_object_or_404(Book, id=cart_item_id)
            if not cart:
                cart = Cart.objects.create(user=self.request.user)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
            cart_item.quantity += 1
            cart_item.save()
            cart.calculate_total_price()

        elif action == 'remove':
            if not cart:
                raise Http404("Cart not found")

            cart_item = CartItem.objects.filter(cart=cart, book_id=cart_item_id).first()
            if not cart_item:
                raise Http404("CartItem not found")

            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()

            cart.calculate_total_price()

        else:
            if not cart:
                cart = None

        context['cart'] = cart
        return context
