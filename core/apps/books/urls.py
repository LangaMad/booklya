from django.urls import path
from .views  import *

urlpatterns = [
    path('book_detail_1/', BookDetailView1.as_view(), name='book_detail_1'),
    path('book_list/', BookListView.as_view(), name='book_list'),
] 