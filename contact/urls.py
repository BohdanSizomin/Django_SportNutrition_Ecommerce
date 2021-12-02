from django.urls import path, include
from . import views

urlpatterns = [
    # /home
    path('', views.contact, name='contact'),
    path('success', views.success, name='success'),
    path('failure', views.failure, name='failure'),
]
