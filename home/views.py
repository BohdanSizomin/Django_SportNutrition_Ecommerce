from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "title": "Welcome to our sport nutrition shop",
        "keywords": "ecommerce,sport nutrition,buy sport nutrition,protein buy"
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
