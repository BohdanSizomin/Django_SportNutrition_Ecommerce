from django.forms import ModelForm
from django import forms
from .models import Contact


class ContactForm(ModelForm):
    email = forms.EmailField(required=True, label='email', widget=forms.TextInput(attrs={
        'autocomplete': 'off'
    }))
    subject = forms.CharField(max_length=50, required=True, label='subject', widget=forms.TextInput(attrs={
        'autocomplete': 'off'
    }))
    message = forms.CharField(max_length=500, required=True, label='message', widget=forms.Textarea(
        attrs={'message': 'Type your message here...'}))

    class Meta:
        model = Contact
        fields = ('email', 'subject', 'message')
