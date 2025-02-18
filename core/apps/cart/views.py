from venv import create
from django.shortcuts import render
from .models import Cart,CartItem
from django.views import View
from ..books.models import Book



class CartView(View):
    def cart_add(self,request,book_id):
        book = Book.objects.all(id=book_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.gett_or_create(cart=cart, book=book)
        cart_item.quantity += 1
        cart_item.save()
        cart.calculate_total_price()
        return render(request, 'pages/cart.html', {'cart':cart})

    def cart_remove(self,request,cart_item_id):
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()
        cart = Cart.objects.get(user=request.user)
        cart.calculate_total_price()
        return render(request, 'pages/cart.html', {'cart':cart})

    def get(self,request,action,cart_item_id):
        if action == 'add':
            return self.cart_add(request, cart_item_id)
        elif action == 'remove':
            return self.cart_remove(request, cart_item_id)
        else:
            return render(request, 'pages/cart.html', {'cart':None})



