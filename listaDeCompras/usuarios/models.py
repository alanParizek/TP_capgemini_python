from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    chango = models.ForeignKey(
        'carrito.Chango',
        on_delete=models.CASCADE, # REVISAR
        null=True
    )