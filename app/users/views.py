from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import SignupForm


def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users:home")

    return render(
        request,
        "users/signup.html",
        {"form": form},
    )


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("users:home")
        else:
            # message.info(request, "invalid credentials")
            return redirect("users:login")
    else:
        return render(
            request,
            "users/login.html",
        )


@login_required
def logout_user(request):
    logout(request)
    return render(
        request,
        "users/login.html",
    )


@login_required
def home(request):
    return render(request, "users/home.html")
