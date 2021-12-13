from django.urls import path, include
from . import views

urlpatterns = [
    # /home
    path('login/', views.login, name='login'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),

    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('forgotPassword', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword', views.resetPassword, name='resetPassword')
]
