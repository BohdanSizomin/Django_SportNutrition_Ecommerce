from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post, UserTrainer


# Create your views here.

# настроить вьюху,сделать миграции,настроить шаблоны для прложения блог,добавитть тренеров,добавить посты
class PostListView(ListView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'post'
    paginate_by = 3
