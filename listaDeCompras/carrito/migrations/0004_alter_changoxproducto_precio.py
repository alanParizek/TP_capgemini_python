# Generated by Django 4.1.3 on 2022-12-07 18:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0003_changoxproducto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changoxproducto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=25, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
