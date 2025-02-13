from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import ContactUsForm

class HomeView(TemplateView):
    template_name = 'pages/index.html'
#
class ContactUs(CreateView):
    template_name = 'pages/contact_us.html'
    form_class = ContactUsForm
    success_url = '/'