from django.shortcuts import render
from django.views import View
from .models import Cart, CartItem
from ..books.models import Book
# Create your views here.



class CartView(View):
    # def get(self, requests, action, item_id):
    #     cart = Cart.objects.get(user=request.user)
    #     if action == 'add':
    #         item = CartItem.objects.get(id = item_id)
    #         item.quantity += 1
    #         item.save()
    def cart_add(self, request, book_id):
        book = Book.object.get(id=book_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item = created = CartItem.objects.get_or_create(cart=cart, book=book)
        cart_item.quantity += 1
        cart_item.save()
        cart.calculate_total_price()
        return render(request, 'page/cart.html', {'cart': cart})

    def cart_remove(self, request, cart_itema_id):
        cart_item = CartItem.objects.get(id=cart_itema_id)
        cart_item.delete()
        cart = Cart.objects.get(user=request.user)
        cart.calculate_total_price()
        return render(request, 'page/cart.html', {'cart': cart})

    def get(self, request, action, cart_item_id):
        if action == 'add':
            return self.cart_add(request, cart_item_id)
        elif action == 'remove':
            return  self.cart_remove(request, cart_item_id)
        else:
            return render(request, 'page/cart.html', {'cart': None})