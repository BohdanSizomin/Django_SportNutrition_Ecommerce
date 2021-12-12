from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from home.models import *
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


# Create your views here.
def index(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')

        # Pagination
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        products_count = products.count()

    context = {
        "title": "Welcome to our sport nutrition shop",
        "keywords": "ecommerce,sport nutrition,buy sport nutrition,protein buy",
        "products": paged_products,
        "products_count": products_count,
    }
    return render(request, 'index.html', context)


def contact(request):
    context = {
        "title": "How to contact us",
    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        "title": "About us",
    }
    return render(request, 'about.html', context)


def what_to_choose(request):
    context = {
        "title": "Don`t know how to choose sport nutrition ?",
    }
    return render(request, 'whattochoose.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)

        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,

    }
    return render(request, 'product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-create_date').filter(Q(description__icontains=keyword) |
                                                                       Q(name__icontains=keyword))
            products_count = products.count()
    context = {
        'products': products,
        'products_count': products_count,
    }

    return render(request, 'index.html', context)
