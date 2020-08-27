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
    BlogSearch,
)

from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('search/', BlogSearch.as_view(), name='search'),
    re_path(r'^manage/update/(?P<pk>\d+)$',
            BlogUpdate.as_view(), name='update'),
    re_path(r'^manage/delete/(?P<pk>\d+)$',
            BlogDelete.as_view(), name='delete'),
    path('manage/', BlogManage.as_view(), name='manage'),
    path('tambah/', BlogCreate.as_view(), name='create'),
    re_path(r'^kategori/(?P<slug>[\w-]+)/(?P<page>\d+)$',
            BlogCategory.as_view(), name='category'),
    re_path(r'^detail/(?P<slug>[\w-]+)$', BlogDetail.as_view(), name='detail'),
    re_path(r'^(?P<page>\d+)$', BlogList.as_view(), name='list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
