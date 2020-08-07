from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from django.contrib.auth.models import User


class UserRegister(UserCreationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'username'}))
    first_name = forms.CharField(label="First Name", max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'firstname'}))
    last_name = forms.CharField(label="Last Name", max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'lastname'}))
    email = forms.EmailField(label="Email", max_length=30,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'email'}))
    password1 = forms.CharField(label="Password", max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'id': 'password'}))
    password2 = forms.CharField(label="Password confirmation", max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'id': 'password'}))

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'email',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'type': 'text', 'id': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'type': 'password', 'id': 'password'}))
