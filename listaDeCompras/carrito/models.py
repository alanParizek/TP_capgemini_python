from django.db import models

class Chango(models.Model):
    def agregarProducto(self, producto, cantidad=1):
        pass
    def sacarCantProducto(self, producto, cantidad=1):
        pass
    def sacarTodosDeUnProducto(self, producto):
        pass
    def vaciar(self):
        pass
    

class changoXproducto(models.Model):
    chango = models.ForeignKey(
        'carrito.Chango',
        on_delete=models.CASCADE,
        )
    producto = models.ForeignKey(
        'productos.Producto',
        on_delete=models.CASCADE,
        )
    cantidad = models.IntegerField()