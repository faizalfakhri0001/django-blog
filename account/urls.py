from django.contrib import admin
from django.urls import path, include, re_path

from blog.models import Artikel
from .views import(
    UserRegistration,
    UserLogin,
)

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
]
