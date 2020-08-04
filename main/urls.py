from django.contrib import admin
from django.urls import path, include, re_path

from .views import Home
from blog.models import Artikel

urlpatterns = [
    path('blog/', include('blog.urls', namespace='blog')),
    path('', Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
