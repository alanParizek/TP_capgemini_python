# Generated by Django 4.1.3 on 2022-12-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_alter_changoxproducto_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='changoxproducto',
            name='precio',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
