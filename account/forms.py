from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.contrib.auth.models import User
from .models import Profile


class UserRegister(UserCreationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'username'}))
    first_name = forms.CharField(label="First Name", max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'firstname'}))
    last_name = forms.CharField(label="Last Name", max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'lastname'}))
    email = forms.EmailField(label="Email", max_length=30,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'email'}))

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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'Description', 'website_name', 'website_url', 'facebook_name', 'facebook_url',
                  'whatsapp_number', 'instagram_name', 'instagram_url', 'pinterest_name', 'pinterest_url', 'github_name', 'github_url']

        widgets = {
            'image': forms.FileInput(attrs={'class': 'custom-file'}),
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'website_name': forms.TextInput(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_name': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_name': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'pinterest_name': forms.TextInput(attrs={'class': 'form-control'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
            'github_name': forms.TextInput(attrs={'class': 'form-control'}),
            'github_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
