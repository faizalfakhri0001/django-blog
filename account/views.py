from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
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
from django.contrib.auth.mixins import LoginRequiredMixin


class UserProfile(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'registration/profile.html'
    context_object_name = 'profile'

    def get_context_data(self, *args, **kwargs):
        user = self.model.objects.get(user=self.request.user)
        artikel_list = user.user.artikel.all()

        self.kwargs.update({'artikels': artikel_list[0:3]})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class UserProfileEdit(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/profile_update.html'

    def get(self, request, *args, **kwargs):
        if int(self.request.user.profile.id) != int(self.kwargs['pk']):
            return redirect('profile')
        return super().get(request, *args, **kwargs)


class UserRegistration(CreateView):
    form_class = UserRegister
    template_name = 'registration/user_register.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        else:
            self.object = None
            return super().get(request, *args, **kwargs)

class UserLogin(LoginView):
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        if self.request.user.is_authenticated:
            return redirect('home')
        else:
            return self.render_to_response(self.get_context_data())
