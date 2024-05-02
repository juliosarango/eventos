# Generated by Django 4.2.11 on 2024-04-30 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("eventos", "0002_boletos_estado_vendedor_alter_boletos_usuario_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Premios",
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
                ("numero_premio", models.PositiveSmallIntegerField(default=0)),
                ("descripcion_premio", models.TextField(default="", null=True)),
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
                "verbose_name": "Premio",
                "verbose_name_plural": "Premios",
                "db_table": "premios",
                "ordering": ["id"],
            },
        ),
    ]
