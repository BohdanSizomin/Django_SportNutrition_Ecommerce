from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import article

urlpatterns = [
    path('', views.article, name='article'),
]