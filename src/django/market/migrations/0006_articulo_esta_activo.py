# Generated by Django 5.1.7 on 2025-07-13 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_articulo_comprador'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='esta_activo',
            field=models.BooleanField(default=True),
        ),
    ]
