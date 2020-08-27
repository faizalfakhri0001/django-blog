from django.contrib import admin
from django.urls import path, include, re_path

from blog.models import Artikel
from .views import(
    UserRegistration,
    UserLogin,
    UserProfile,
    UserProfileEdit
)

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    re_path(r'^profile/$',
            UserProfile.as_view(), name='profile'),
    re_path(r'^profile/edit/(?P<pk>\d+)$',
            UserProfileEdit.as_view(), name='profile_edit'),
]
