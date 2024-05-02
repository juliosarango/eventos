from django.db.models import Q

from app.apps.eventos.models import Boletos


class Utils:

    def generar_boletos(self, evento, cantidad, vendedor, usuario):
        boleto = Boletos()
        for i in range(1, cantidad + 1):
            boleto = Boletos.objects.create(
                evento=evento,
                numero=i,
                vendedor=vendedor,
                usuario=usuario,
            )

        boleto.save()


class NotificacionesEmail:
    datos = {
        "REGISTRO_EXITOSO": {
            "subject": "Registro correcto, bienvenido!",
            "template": "emails/activar_usuario.html",
        }
    }
