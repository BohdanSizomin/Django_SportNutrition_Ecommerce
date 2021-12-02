from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Contact
from .forms import ContactForm


# Create your views here.
def contact(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            return redirect('failure')

    form = ContactForm()
    context = {
        'form': form,
        'title': 'Contact us !',
    }
    return render(request, 'contact.html', context)


def success(request):
    return render(request, 'contact_success.html')


def failure(request):
    return render(request, 'contact_failure.html')


