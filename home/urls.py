from django.urls import path, include
from . import views

urlpatterns = [
    # /home
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('what_to_choose', views.what_to_choose, name='what_to_choose'),
    path('blog/', include('blog.urls')),

]
