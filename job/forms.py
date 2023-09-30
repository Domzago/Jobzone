from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Job

class CreateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email Address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}))


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your Password'}))
