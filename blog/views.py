from django.shortcuts import render
from .models import Post


# Create your views here.

# настроить вьюху,сделать миграции,настроить шаблоны для прложения блог,добавитть тренеров,добавить посты
def articles(request):
    return render('Hello')


def article_detail(request):
    pass
