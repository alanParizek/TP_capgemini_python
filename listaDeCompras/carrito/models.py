from django.db import models
from productos import Producto

# SACAR LA CLASE CHANGO Y USAR SOLO CHANGOXPR
class Chango(models.Model):
    def agregarProducto(self, producto: Producto, cantidad=1):
        cXp = ChangoXproducto(chango=self, producto=producto, cantidad=cantidad)
        cXp.save()

    def sacarCantProducto(self, producto: Producto, cantidad=1):
        pass
    
    def sacarTodosDeUnProducto(self, producto: Producto):
        pass
    
    def vaciar(self):
        pass
    

class ChangoXproducto(models.Model):
    chango = models.ForeignKey(
        'carrito.Chango',
        on_delete=models.CASCADE,
        )
    producto = models.ForeignKey(
        'productos.Producto',
        on_delete=models.CASCADE,
        )
    cantidad = models.IntegerField()