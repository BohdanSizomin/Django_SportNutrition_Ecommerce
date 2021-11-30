from django.contrib.auth.forms import UserCreationForm

from .models import UserTrainer


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserTrainer
        fields = "__all__"
