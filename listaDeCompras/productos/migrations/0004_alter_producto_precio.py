# Generated by Django 4.1.3 on 2022-12-07 18:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_productocontable_productoengramos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=25, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
