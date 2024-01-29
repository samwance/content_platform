from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import Login, Register, UserRetrieve, ProfileUser, logout_user

app_name = UsersConfig.name

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", Register.as_view(), name="register"),
    path("profile/", ProfileUser.as_view(), name="profile"),
    path("profile/<pk>/", UserRetrieve.as_view(), name="user_retrieve"),
]
