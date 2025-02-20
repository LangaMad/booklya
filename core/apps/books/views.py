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
    paginate_by = 3

    def get_queryset(self):
        queryset = Book.objects.all()
        order_by = self.request.GET.get('order_by')
        if order_by:
            if order_by == 'popularity':
                queryset = queryset.order_by('-rate')
            elif order_by == 'rate':
                queryset = queryset.order_by('-rate')
            elif order_by == 'newest':
                queryset = queryset.order_by('-created_at')
            elif order_by == 'price':
                queryset = queryset.order_by('price')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_language'] = BookLanguage.objects.all()
        context['genres'] = Genre.objects.all()[:3]
        context['authors'] = Book.objects.values_list('author', flat=True).distinct()[:3]
        context['tags'] = Tag.objects.all()[:3]
        context['book_price'] = Book.objects.order_by('price')[:6]
        context['popular'] = Book.objects.order_by('rate')[:4]
        context['new_releases'] = Book.objects.order_by('-created_at')[:6]
        context['on_order'] = Book.objects.order_by('created_at')
        return context



class BookDetailView1(DetailView):
    model = Book
    template_name = 'pages/book_detail.html'
    queryset = Book.objects.all()
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_languages'] = BookLanguage.objects.filter(book=self.object)
        context['book_language'] = BookLanguage.objects.all()
        context['genres'] = Genre.objects.all()[:3]
        context['authors'] = Book.objects.values_list('author', flat=True).distinct()[:3]
        context['tags'] = Tag.objects.all()[:3]
        context['book_price'] = Book.objects.order_by('price')[:6]
        context['popular'] = Book.objects.order_by('rate')[:4]
        context['new_releases'] = Book.objects.order_by('-created_at')[:6]
        context['on_order'] = Book.objects.order_by('created_at')
        return context