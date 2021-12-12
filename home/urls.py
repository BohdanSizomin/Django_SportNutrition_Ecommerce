from django.urls import path, include
from . import views

urlpatterns = [
    # /home
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('what_to_choose', views.what_to_choose, name='what_to_choose'),

    path('store/<slug:category_slug>/', views.index, name='products_by_category'),
    path('store/<slug:category_slug>/<slug:product_slug>', views.product_detail, name='product_detail'),
    path('search', views.search, name='search'),
    # path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('authentication/', include('users.urls')),

    path('cart/', include('cart.urls')),

]
