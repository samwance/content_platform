from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from content.models import Content
from users.forms import ProfileUserForm, LoginUserForm, RegisterUserForm
from users.models import User


class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Authorization'}

    def get_success_url(self):
        return reverse_lazy("users:profile")


def logout_user(request):
    logout(request)
    return redirect('users:login')


class Register(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    extra_context = {'title': "Registration"}
    success_url = reverse_lazy("content:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(phone=form.cleaned_data['phone'], password=form.cleaned_data['password1'])
        if user is not None:
            login(self.request, user)
        return response


class UserRetrieve(DetailView):
    model = User
    template_name = "users/user_retrieve.html"
    extra_context = {"title": "User's profile"}

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get("pk"))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        context["title"] = user.name
        context["posts"] = Content.objects.filter(user=user)
        return context


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {
        'title': "Edit profile",
    }

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
