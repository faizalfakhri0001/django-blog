from django import forms
from .models import Artikel


class AddForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul', 'thumbnail', 'isi', 'author', 'kategori']

        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'custom-file'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'kategori': forms.Select(attrs={'class': 'form-control'})
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul', 'isi', 'kategori']

        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'kategori': forms.TextInput(attrs={'class': 'form-control'})
        }
