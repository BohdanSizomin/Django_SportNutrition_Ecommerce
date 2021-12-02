from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import *


# Create your views here.
def login(request):
    context = {}
    return render(request, '', context)


def sign_up(request):
    context = {}
    return render(request, '', context)
