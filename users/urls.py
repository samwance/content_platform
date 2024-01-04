from django.urls import path

from users.apps import UsersConfig
from users.views import Login, Register, Logout, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path("", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("register/", Register.as_view(), name="register"),
]