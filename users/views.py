from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserForm, UserRegisterForm
from users.models import User


class Login(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("content:index")


class Logout(LogoutView):
    pass


class Register(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("content:index")


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm


    # Перенаправление на обновленную страницу профиля
    def get_success_url(self):
        return reverse_lazy("users:profile", kwargs={"pk": self.object.pk})
