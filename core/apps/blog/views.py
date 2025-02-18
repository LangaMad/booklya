from django.shortcuts import render ,get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Post, PostCommentary
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.
class BlogView(ListView):
    model = Post
    template_name = 'pages/blog.html'
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by()
    paginate_by = 3

    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return Post.objects.all()
        q = Post.objects.filter(Q(title__icontains= search_text)|Q(text__icontains= search_text))
        return q

class DetailBlogView(DetailView):
    template_name = 'pages/blog_detail.html'
    model = Post
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.post_comments.all()  # Add comments to the context
        return context

class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user if request.user.is_authenticated else None
        comment_text = request.POST.get('comment_text')
        PostCommentary.objects.create(post=post, user=user, comment_text=comment_text)
        return redirect('blog_detail', pk=post_id)