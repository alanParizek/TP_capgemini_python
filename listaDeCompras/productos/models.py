from django.core.validators import MinValueValidator
from django.db import models
from model_utils.managers import InheritanceManager
# Create your models here.

class TipoDeCalculoEquivocado(Exception):
    pass

# ESTO ES UNA CLASE ABSTRACTA, NO LA INSTANCIES
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=25, decimal_places=2, validators=[MinValueValidator(0)])

    objects = InheritanceManager()
    # permite usar .select_subclasses() para que instancie las subclases en lugar de Producto

    def __str__(self):
        producto = Producto.objects.get_subclass(pk=self.pk)
        return self.nombre + ' - ' + producto.unidad
        
    def precioRedondeado(self, cantidad) -> float:
        return round(self.calcularPrecio(cantidad), 2)

    @classmethod
    def listaDePrecios(cls):
        return map(
            lambda producto: (producto.pk, producto.calcularPrecio(1)),
            Producto.objects.all().select_subclasses()
        )

class ProductoContable(Producto):
    unidad = 'unidad/es'
    
    def calcularPrecio(self, cantidad) -> float:
        return self.precio * cantidad

    @staticmethod
    def cantidad(cantidad: int):
        return cantidad

class ProductoEnGramos(Producto):
    unidad = 'gramos'
        
    def calcularPrecio(self, cantidad) -> float:
        return self.precio * cantidad/100

    @staticmethod
    def cantidad(cantidad: int):
        return None