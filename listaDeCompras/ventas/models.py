from django.db import models
from datetime import date
from django.conf import settings
import json
# Create your models here.


class Venta(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    jsonText = models.TextField()
    
    @staticmethod
    def registrarVenta(carrito):
        json = Venta.crearTextoJson(carrito)
        venta = Venta(carrito.usuario, json)
        venta.save()
        # arma la venta con el carrito y la guarda en la DB
    
    @staticmethod
    def crearTextoJson(carrito) -> str:
        dictJson = carrito.__dict__
        dictJson['idCarrito'] = dictJson.pop('id') #Cambiando nombre a la key id del carrito
        dictJson.pop('fuePagado')
        items = map(
            lambda changoXprod: {'producto': changoXprod.producto.nombre, 
                'cantidad': changoXprod.cantidad,
                'precio': changoXprod.precio,
                'id': changoXprod.producto.pk},
            carrito.getProductos()
            )
        dictJson['total'] = carrito.total()
        dictJson['items'] = items
        dictJson['nombre'] = carrito.usuario.first_name
        dictJson['usuario'] = carrito.usuario.last_name
        return json.dumps(dictJson)
