from django.urls import path
from .views  import *

urlpatterns = [
    path('book_detail/<int:pk>/', BookDetailView1.as_view(), name='book_detail'),
    path('book_list/', BookListView.as_view(), name='book_list'),
]