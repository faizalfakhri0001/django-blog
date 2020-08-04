from django import forms
from .models import Artikel


class AddForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul', 'isi', 'kategori']
    
