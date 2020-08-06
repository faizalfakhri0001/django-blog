from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
    ListView,
)
from django.contrib.auth.views import(
    LoginView,
)
from .forms import(
    UserRegister,
    LoginForm,
)


class UserRegistration(CreateView):
    form_class = UserRegister
    template_name = 'registration/user_register.html'
    success_url = reverse_lazy('login')


class UserLogin(LoginView):
    form_class = LoginForm
