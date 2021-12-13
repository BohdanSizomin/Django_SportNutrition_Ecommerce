from .models import Account
from django import forms


class SigupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'autocomplete': 'off',

    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={

        'autocomplete': 'off',

    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(SigupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone_number'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter password'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm password'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['autocomplete'] = 'off'

    def clean(self):
        cleaned_data = super(SigupForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not match'
            )
