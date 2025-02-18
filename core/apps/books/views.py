from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import *
# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'pages/book_list.html'
    context_object_name = 'books'
    queryset = Book.objects.all()
    paginate_by = 6

class BookDetailView1(DetailView):
    model = Book
    template_name = 'pages/book_detail_1.html'
    context_object_name = 'book1'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_languages'] = BookLanguage.objects.filter(book=self.object)
        return context