from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post, UserTrainer


# Create your views here.

# настроить вьюху,сделать миграции,настроить шаблоны для прложения блог,добавитть тренеров,добавить посты
def article(request):
    return render(request, 'article.html')
