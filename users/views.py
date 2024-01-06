from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from users.forms import ProfileUserForm, LoginUserForm, RegisterUserForm
from users.models import User


class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy("users:profile")


def logout_user(request):
    logout(request)
    return redirect('users:login')


class Register(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy("content:index")


class UserRetrieve(DetailView):
    Model = User
    template_name = "users/profiles.html"

    def get_object(self, queryset=None):
        return self.request.user


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {
        'title': "User's profile",
    }

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
