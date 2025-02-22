from django.views.generic import TemplateView, ListView, DetailView
from .models import BookNews



# Create your views here.
class NewsView(ListView):
    model = BookNews
    template_name = 'pages/news_list.html'
    context_object_name = 'news'
    queryset = BookNews.objects.all().order_by('-created_at')
    paginate_by = 3



class DetailNewsView(DetailView):
    template_name = 'pages/news_detail.html'
    model = BookNews
    context_object_name = 'new'
    queryset = BookNews.objects.all()