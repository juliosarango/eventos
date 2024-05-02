from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path(
        "signup",
        views.signup,
        name="signup",
    ),
    path(
        "home",
        views.home,
        name="home",
    ),
    path(
        "login",
        views.login_user,
        name="login",
    ),
    path(
        "logout",
        views.logout_user,
        name="logout",
    ),
    path(
        "activate/<uidb64>/<token>/",
        views.activar_usuario,
        name="activate",
    ),
    path(
        "users/update/",
        views.update_user,
        name="update",
    ),
]
