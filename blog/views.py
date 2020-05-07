from django.shortcuts import render

# Create your views here.
from .models import Artikel

class LastUpdateArtikel():
    model = Artikel

    def latest_artikel(self):
        last_artikel = self.model.objects.values_list('kategori', flat=True).distinct()
        queryset = []
        
        for artikels in last_artikel:
            artikel = self.model.objects.filter(kategori=artikels).latest('published')
            queryset.append(artikel)
        
        return queryset