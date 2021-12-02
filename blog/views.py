from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView, DetailView
from .models import Post, UserTrainer
from django.template import RequestContext


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'article.html'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post.html'
