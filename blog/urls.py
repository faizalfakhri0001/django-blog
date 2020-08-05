from django.contrib import admin
from django.urls import path, include, re_path

from blog.models import Artikel
from .views import(
    BlogList,
    BlogDetail,
    BlogCategory,
    BlogCreate,
    BlogManage,
    BlogDelete,
    BlogUpdate,
)

app_name = 'blog'

urlpatterns = [
    re_path(r'^manage/update/(?P<pk>\d+)$',
            BlogUpdate.as_view(), name='update'),
    re_path(r'^manage/delete/(?P<pk>\d+)$',
            BlogDelete.as_view(), name='delete'),
    path('manage/', BlogManage.as_view(), name='manage'),
    path('tambah/', BlogCreate.as_view(), name='create'),
    re_path(r'^kategori/(?P<kategori>[\w]+)/(?P<page>\d+)$',
            BlogCategory.as_view(), name='category'),
    re_path(r'^detail/(?P<slug>[\w-]+)$', BlogDetail.as_view(), name='detail'),
    re_path(r'^(?P<page>\d+)$', BlogList.as_view(), name='list'),
]
