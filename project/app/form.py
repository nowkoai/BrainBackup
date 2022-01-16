from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(required=False)
    password2 = password1

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
