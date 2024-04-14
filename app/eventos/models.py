from django.db import models
from django.db import models
from django.conf import settings


class TipoEvento(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(
        "fecha registro",
        null=False,
        auto_now_add=True,
        help_text="Fecha registro",
    )

    def __str__(self) -> str:
        return f"{self.nombre}"

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ["fecha_registro"]
        db_table = "tipo_evento"


class Evento(models.Model):

    def path_to_upload(instance, filename):
        return "user_{0}_{1}".format(instance.user.id, filename)

    organizador = models.CharField(max_length=500, null=False)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=1000, null=False)
    cantidad_boletos = models.SmallIntegerField(
        null=False,
        default=0,
    )
    fecha_hora = models.DateTimeField(
        "fecha y hora del evento",
        null=False,
        auto_now_add=False,
        help_text="Fecha y hora del evento",
    )
    valor = models.FloatField()
    arte = models.ImageField(upload_to="artes/%Y-%m-%d")
    estado = models.BooleanField(default=True)
    publicado = models.BooleanField(default=False)
    tipo = models.ForeignKey(
        TipoEvento,
        on_delete=models.CASCADE,
        null=False,
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
    )

    fecha_registro = models.DateTimeField(
        "fecha registro",
        null=False,
        auto_now_add=True,
        help_text="Fecha registro",
    )

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["-fecha_registro"]
        db_table = "eventos"
