from django.views.generic import TemplateView, ListView, DetailView
from .models import BookNews



# Create your views here.
class NewsView(ListView):
    model = BookNews
    template_name = 'pages/news_list.html'
    context_object_name = 'news'
    queryset = BookNews.objects.all().order_by()
    paginate_by = 4

    # def post_list(request):
    #     # Получаем все посты
    #     posts = BookNews.objects.all()
    #
    #     # Настроим пагинацию
    #     paginator = Paginator(posts, 5)  # Показывать по 5 постов на странице
    #     page_number = request.GET.get('page')  # Получаем номер текущей страницы
    #     page_obj = paginator.get_page(page_number)
    #
    #     return render(request, 'your_template.html', {'page_obj': page_obj})

class DetailNewsView(DetailView):
    template_name = 'pages/news_detail.html'
    model = BookNews
    context_object_name = 'new'
    queryset = BookNews.objects.all()