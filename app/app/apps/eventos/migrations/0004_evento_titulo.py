# Generated by Django 4.2.11 on 2024-04-30 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventos", "0003_premios"),
    ]

    operations = [
        migrations.AddField(
            model_name="evento",
            name="titulo",
            field=models.CharField(default="Prueba", max_length=300),
            preserve_default=False,
        ),
    ]