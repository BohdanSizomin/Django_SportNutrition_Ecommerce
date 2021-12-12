from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def login(request):
    pass

    context = {}
    return render(request, 'login.html', context)


def sign_up(request):
    context = {
        'title': 'Log in page',

    }
    return render(request, 'signup.html', context)


def profile(request):
    context = {}
    return render(request, 'profile.html', context)


def logout(request):
    pass
