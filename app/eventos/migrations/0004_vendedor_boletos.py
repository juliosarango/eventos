# Generated by Django 4.2.11 on 2024-04-15 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("eventos", "0003_alter_evento_arte"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vendedor",
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
                ("estado", models.BooleanField(default=True)),
                (
                    "fecha_registro",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Fecha registro",
                        verbose_name="fecha registro",
                    ),
                ),
                (
                    "evento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="eventos.evento"
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Vendedor",
                "verbose_name_plural": "Vendedores",
                "db_table": "vendedor",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Boletos",
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
                ("numero", models.PositiveIntegerField(default=0)),
                (
                    "fecha_registro",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Fecha registro",
                        verbose_name="fecha registro",
                    ),
                ),
                (
                    "evento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="eventos.evento"
                    ),
                ),
            ],
            options={
                "verbose_name": "Boleto",
                "verbose_name_plural": "Boletos",
                "db_table": "boletos",
                "ordering": ["id"],
            },
        ),
    ]
