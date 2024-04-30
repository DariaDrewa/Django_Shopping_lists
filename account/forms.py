from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=255, help_text="Pole wymagane.")

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email)
        except Exception:
            return email
        raise forms.ValidationError(f"Adres e-mail '{email}' jest już zajęty.")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.get(username=username)
        except Exception:
            return username
        raise forms.ValidationError(f"Nazwa użytkownika '{username}' jest już zajęta.")
