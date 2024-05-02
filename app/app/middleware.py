from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse


class UsuarioMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if (
            not request.user.is_anonymous
            and not request.user.is_staff
            and not request.user.datos_actualizados
            and request.path not in [reverse("users:logout")]
            and request.path not in [reverse("users:login")]
            and request.path
            not in [
                reverse(
                    "users:update",
                    # args=[request.user.id],
                )
            ]
        ):
            return redirect("users:update")

        response = self.get_response(request)

        return response
