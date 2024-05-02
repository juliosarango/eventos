from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.forms import modelformset_factory
from .models import Evento, TipoEvento, Premios


class EventoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tipo"].queryset = TipoEvento.objects.filter(estado=True)

    class Meta:
        model = Evento
        fields = [
            "organizador",
            "titulo",
            "descripcion",
            "fecha_hora",
            "direccion",
            "valor",
            "cantidad_boletos",
            "tipo",
            "arte",
        ]

        labels = {
            "organizador": "Quién organiza el evento: Ejm. Grupo de amigos",
            "descripcion": "Descripción del evento",
            "fecha_hora": "Fecha y hora del evento",
            "direccion": "Dirección donde se realizará el evento",
            "valor": "Valor de cada boleto",
            "cantidad_boletos": "Cantidad de boletos que se generarán",
            "tipo": "Tipo de evento",
            "arte": "Diseño gráfico del evento",
        }

        widgets = {
            "tipo": forms.widgets.Select(
                attrs={
                    "class": "form-control form-control-sm",
                    "required": True,
                }
            ),
        }


PremiosFormSet = modelformset_factory(
    Premios,
    fields=("numero_premio", "descripcion_premio"),
    extra=1,
)
