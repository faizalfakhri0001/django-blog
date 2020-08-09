from django.contrib import admin
from django.urls import path, include, re_path

from .views import Home
from blog.models import Artikel

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    re_path(r'^$', Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
