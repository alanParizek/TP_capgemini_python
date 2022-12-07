from django.db import models
from model_utils.managers import InheritanceManager
# Create your models here.

class TipoDeCalculoEquivocado(Exception):
    pass

# ESTO ES UNA CLASE ABSTRACTA, NO LA INSTANCIES
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        producto = Producto.objects.get_subclass(pk=self.pk)
        return self.nombre + ' - ' + producto.unidad
        
    
    # permite usar .select_subclasses() para que instancie las subclases en lugar de Producto
    objects = InheritanceManager()
    
class ProductoContable(Producto):
    unidad = 'unidad/es'
    
    def calcularPrecio(self, cantidad):
        return self.precio * cantidad

    def cantidad(self, cantidad: int):
        return cantidad

class ProductoEnGramos(Producto):
    unidad = 'gramos'
        
    def calcularPrecio(self, cantidad):
        return self.precio * cantidad/100

    def cantidad(self, cantidad: int):
        return None