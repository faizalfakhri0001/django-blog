from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from blog.views import LastUpdateArtikel
from blog.models import Artikel

# Create your views here.


class Home(TemplateView, LastUpdateArtikel):
    template_name = "index.html"

    def get_context_data(self):
        querysets = self.latest_artikel()
        context = {
            'last_artikel': querysets,
        }
        return context
