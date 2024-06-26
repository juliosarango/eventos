# Generated by Django 4.2.11 on 2024-04-11 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_alter_evento_table_alter_tipoevento_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='cantidad_boletos',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evento',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]
