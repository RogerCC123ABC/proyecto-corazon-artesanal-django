# Generated by Django 4.2.5 on 2023-12-03 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_de_Inventario', '0002_alter_obra_id_artesano'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='cantidadExistente',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
