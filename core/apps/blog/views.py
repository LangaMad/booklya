from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class BlogView(TemplateView):
    template_name = 'pages/blog.html'

class DetailBlogView(TemplateView):
    template_name = 'pages/blog_detail.html'