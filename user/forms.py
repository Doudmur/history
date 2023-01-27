from django.contrib.auth.forms import AuthenticationForm
from user.models import User
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Login'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))
    class Meta:
        model = User
        fields = ('username', 'password')