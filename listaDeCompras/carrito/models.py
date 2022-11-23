from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
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
        '.Chango',
        on_delete=models.CASCADE, # REVISAR
        )
    producto = models.ForeignKey(
        'productos.Producto',
        on_delete=models.CASCADE, # REVISAR
        )
    cantidad = models.DecimalField(max_digits=None, decimal_places=None)