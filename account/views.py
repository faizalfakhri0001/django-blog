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
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .forms import(
    UserRegister,
    LoginForm,
    ProfileForm,
)

from .models import (
    Profile,
)

from django.contrib.auth.models import User


class UserProfile(ListView):
    model = Profile
    template_name = 'registration/profile.html'
    context_object_name = 'profile'

    def get_context_data(self, *args, **kwargs):
        user = self.model.objects.get(id=self.kwargs['pk'])
        artikel_list = user.user.artikel.all()

        self.kwargs.update({'artikels': artikel_list})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class UserProfileEdit(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/profile_update.html'


class UserRegistration(CreateView):
    form_class = UserRegister
    template_name = 'registration/user_register.html'
    success_url = reverse_lazy('login')


class UserLogin(LoginView):
    form_class = LoginForm
    