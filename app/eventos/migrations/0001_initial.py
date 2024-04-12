# Generated by Django 4.2.11 on 2024-04-12 20:05

from django.db import migrations, models
import django.db.models.deletion
import eventos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TipoEvento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("descripcion", models.TextField()),
                ("estado", models.BooleanField(default=True)),
                (
                    "fecha_registro",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Fecha registro",
                        verbose_name="fecha registro",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tipo",
                "verbose_name_plural": "Tipos",
                "db_table": "tipo_evento",
                "ordering": ["fecha_registro"],
            },
        ),
        migrations.CreateModel(
            name="Evento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("organizador", models.CharField(max_length=500)),
                ("descripcion", models.TextField()),
                ("direccion", models.CharField(max_length=1000)),
                ("cantidad_boletos", models.SmallIntegerField(default=0)),
                (
                    "fecha_hora",
                    models.DateTimeField(
                        help_text="Fecha y hora del evento",
                        verbose_name="fecha y hora del evento",
                    ),
                ),
                ("valor", models.FloatField()),
                (
                    "arte",
                    models.ImageField(upload_to=eventos.models.Evento.path_to_upload),
                ),
                ("estado", models.BooleanField(default=True)),
                ("publicado", models.BooleanField(default=False)),
                (
                    "fecha_registro",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Fecha registro",
                        verbose_name="fecha registro",
                    ),
                ),
                (
                    "tipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="eventos.tipoevento",
                    ),
                ),
            ],
            options={
                "verbose_name": "Evento",
                "verbose_name_plural": "Eventos",
                "db_table": "eventos",
                "ordering": ["-fecha_registro"],
            },
        ),
    ]
