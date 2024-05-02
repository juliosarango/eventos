from .celery import app
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse

from app.apps.users.models import User
from app.apps.utils.utils import NotificacionesEmail


@app.task()
def send_email_for_user(user_id, tipo):
    user = User.objects.get(id=user_id)
    print("user==========================", user)
    if user:
        datos = {
            "email": user.email,
            "domain": settings.DOMAIN,
            "site_name": settings.SITE_NAME,
            "protocol": settings.PROTOCOL,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "user": user,
            "token": default_token_generator.make_token(user),
        }
        print(NotificacionesEmail.datos[tipo]["template"])
        email_message = render_to_string(NotificacionesEmail.datos[tipo]["template"], datos)
        return send_email(
            NotificacionesEmail.datos[tipo]["subject"],
            email_message,
            settings.EMAIL_FROM,
            user.email,
        )


def send_email(subject, email_message, from_email, to, bcc=None):
    try:
        email = EmailMessage(
            subject=subject,
            body=email_message,
            from_email=from_email,
            to=[to],
            bcc=bcc,
        )
        email.content_subtype = "html"
        email.send()
        return {"status": "ok", "email": to, "subject": subject}

    except BadHeaderError:
        return HttpResponse("Invalid header found.")
