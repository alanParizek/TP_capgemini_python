# Generated by Django 4.1.3 on 2022-12-11 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0008_rename_fechahorapago_chango_fechahoracierre_and_more'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='usuario',
        ),
        migrations.AddField(
            model_name='venta',
            name='carrito',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='carrito.chango'),
        ),
        migrations.AddField(
            model_name='venta',
            name='fechaHoraPago',
            field=models.DateTimeField(null=True),
        ),
    ]
