from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import UserTrainer


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserTrainer
        fields = "__all__"