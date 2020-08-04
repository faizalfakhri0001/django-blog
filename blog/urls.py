from django.contrib import admin
from django.urls import path, include, re_path

from blog.models import Artikel
from .views import(
    BlogList,
    BlogDetail,
)

app_name = 'blog'

urlpatterns = [
    re_path(r'^detail/(?P<slug>[\w-]+)$', BlogDetail.as_view(), name='detail'),
    re_path(r'^(?P<page>\d+)$', BlogList.as_view(), name='list'),
]
