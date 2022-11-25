from django.db import models

# Create your models here.

class Producto(models.Model):
    precio = models.IntegerField()
    nombre = models.CharField(max_length=100)