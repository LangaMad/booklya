from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

class HomeView(TemplateView):
    template_name = 'pages/index.html'

class ContactUs(TemplateView):
    template_name = 'pages/contact_us.html'
