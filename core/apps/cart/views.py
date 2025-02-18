from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import Cart, CartItem
from ..books.models import Book

class CartGenericView(TemplateView):
    template_name = 'pages/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        action = self.kwargs.get('action')
        cart_item_id = self.kwargs.get('cart_item_id')  # для add это book_id, для remove — cart_item_id

        if action == 'add':
            book = get_object_or_404(Book, id=cart_item_id)
            cart, created = Cart.objects.get_or_create(
                user=self.request.user,
                defaults={'total_price': 0.00}
            )
            cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
            cart_item.quantity += 1
            cart_item.save()
            cart.calculate_total_price()
        elif action == 'remove':
            cart_item = get_object_or_404(CartItem, id=cart_item_id)
            cart_item.delete()
            cart = get_object_or_404(Cart, user=self.request.user)
            cart.calculate_total_price()
        else:
            cart = None

        context['cart'] = cart
        return context
