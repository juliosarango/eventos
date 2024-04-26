from django.db.models import Q

from eventos.models import Boletos, Vendedor


class Utils:
    def asignar_vendedor(self, evento, usuario):

        vendedor = Vendedor.objects.create(
            evento=evento,
            usuario=usuario,
            estado=True,
        )
        vendedor.save()
        return vendedor

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

    # def asignar_boletos_vendedor(self, vendedor, evento, usuario, rango=[]):
    #     boletos = Boletos.objects.filter(
    #         evento=evento, numero__gte=rango[0], numero__lte=rango[1]
    #     )
    #     vendedor = Vendedor.objects.get(id=vendedor.id)
    #     vendedor_boletos = VendedorBoletos()

    #     for i in range(0, rango[1]):
    #         vendedor_boletos = VendedorBoletos.objects.create(
    #             vendedor=vendedor,
    #             boleto=boletos[i],
    #             estado=EstadoBoleto.ASIGNADO,
    #             usuario=usuario,
    #         )
    #     vendedor_boletos.save()


class NotificacionesEmail:
    datos = {
        "REGISTRO_EXITOSO": {
            "subject": "Registro correcto, bienvenido!",
            "template": "emails/activar_usuario.html",
        }
    }
