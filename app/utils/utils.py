from eventos.models import Boletos, Vendedor


class Utils:
    def asignar_vendedor(self, evento, usuario):
        evento = Vendedor.objects.create(
            evento=evento,
            usuario=usuario,
            estado=True,
        )
        evento.save()

    def generar_boletos(self, evento, cantidad):
        boleto = Boletos()
        for i in range(1, cantidad + 1):
            boleto = Boletos.objects.create(
                evento=evento,
                numero=i,
            )

        boleto.save()


class NotificacionesEmail:
    datos = {
        "REGISTRO_EXITOSO": {
            "subject": "Registro correcto, bienvenido!",
            "template": "emails/activar_usuario.html",
        }
    }
