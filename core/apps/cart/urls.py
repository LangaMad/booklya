from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart_detail'),
    path('add/<int:book_id>/', views.CartView.cart_add, name='cart_add'),
    path('remove/<int:cart_item_id>/', views.CartView.cart_remove, name='cart_remove'),
]