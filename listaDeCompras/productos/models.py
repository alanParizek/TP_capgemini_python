from django.db import models

# Create your models here.

class TipoDeCalculoEquivocado(Exception):
    pass

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    # seCalculaEnGramos = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre
    
    # si, para esto tendriamos que usar herencia, pero asi es mas simple
    def calcularPrecioParaUnidades(self, cantidad):
        if self.seCalculaEnGramos:
            raise TipoDeCalculoEquivocado
        else:
            return self.precio * cantidad

class ProductoContable(Producto):
    unidad = 'unidades'
    def calcularPrecioParaUnidades(self, cantidad):
        return self.precio * cantidad

class ProductoEnGramos(Producto):
    unidad = 'gramos'
    def calcularPrecioParaUnidades(self, cantidad):
            return self.precio * cantidad/100