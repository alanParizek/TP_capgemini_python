# Generated by Django 4.1.3 on 2022-12-02 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='seCalculaEnGramos',
            field=models.BooleanField(default=False),
        ),
    ]
