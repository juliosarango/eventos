from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from utils.enums import TipoEmail
from taskapp.task import send_email_for_user
from .forms import SignupForm

User = get_user_model()


def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                print("aqqquiuuuuuiiiiiiiiiiiiiiiiiiiiiiiiiiii")
                send_email_for_user.apply_async(
                    args=(user.id, "REGISTRO_EXITOSO"),
                    countdown=3,
                )
                print("luegpoooooooooooooooooooo")

            return redirect("users:login")

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


def activar_usuario(request, uidb64, token):
    """Activar al usuario

    Activar al usuario con link enviado el email

    Args:
        request (Request): Request de la petición
        uidb64 (str): id del usuario
        token (str): token generado para la validación

    Returns:
        HttpResponse: Retorna el HttpResponse con el mensaje de confirmación
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    message = ""

    if user and default_token_generator.check_token(user, token):
        if not user.is_active:
            user.is_active = True
            user.save()
            message = (
                "Gracias por confirmar su email, su cuenta ha sido habilitada. "
                "Ya puede ingresar al sistema."
            )
        else:
            message = "El usuario ya se encuentra habilitado."
    else:
        message = "¡Link de activación inválido!"
    return render(
        request,
        "users/user_action.html",
        {"message": message},
    )
