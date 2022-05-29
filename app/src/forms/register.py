from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':"floatingInput",
        'placeholder':"nickname"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'id':"floatingPassword",
        'placeholder':"nickname"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'id':"floatingPassword",
        'placeholder':"nickname"
    }))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
