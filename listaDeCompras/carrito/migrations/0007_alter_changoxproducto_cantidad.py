# Generated by Django 4.1.3 on 2022-12-10 14:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0006_rename_fechacreacion_chango_fechahoracreacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changoxproducto',
            name='cantidad',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
