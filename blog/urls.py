from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='article'),

]
