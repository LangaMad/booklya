from tkinter.font import names

from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogView.as_view(), name = 'blog'),
    path('detail/', DetailBlogView.as_view(), name = 'detail_blog'),
]