# Generated by Django 4.1.3 on 2022-12-09 12:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0004_alter_changoxproducto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changoxproducto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=25, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]