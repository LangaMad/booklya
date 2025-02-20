from django.urls import path
from .views import  CartGenericView

urlpatterns = [
    # path('cart/', views.CartGenericView.as_view(), name='cart_detail'),
    # path('add/<int:book_id>/', views.CartGenericView.cart_add, name='cart_add'),
    # path('remove/<int:cart_item_id>/', views.CartView.cart_remove, name='cart_remove'),
    path('cart/<str:action>/<int:cart_item_id>/', CartGenericView.as_view(), name='cart_action'),
]