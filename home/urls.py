from django.urls import path, include
from . import views

urlpatterns = [
    # /home
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),

]
