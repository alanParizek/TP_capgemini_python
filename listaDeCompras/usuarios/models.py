from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)