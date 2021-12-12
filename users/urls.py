from django.urls import path, include
from . import views

urlpatterns = [
    # /home
    path('login/', views.login, name='login'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]
