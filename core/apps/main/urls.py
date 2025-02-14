from tkinter.font import names

from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('contact_us/', ContactUs.as_view(), name = 'contact_us'),
]