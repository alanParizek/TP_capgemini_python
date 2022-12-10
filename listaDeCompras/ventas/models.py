from django.db import models
from datetime import datetime
from django.conf import settings
import json
from productos.models import Producto
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
        venta = Venta(usuario=carrito.usuario, jsonText=json)
        venta.save()
        # arma la venta con el carrito y la guarda en la DB
    
    @staticmethod
    def crearTextoJson(carrito) -> str:
        dictJson = carrito.__dict__.copy()
        dictJson['idCarrito'] = dictJson.pop('id') #Cambiando nombre a la key id del carrito
        dictJson.pop('fuePagado')
        dictJson.pop('_state')
        dictJson.pop('fechaHoraCreacion')
        dictJson['fecha_hora_pago'] = formatearFechaYHora(dictJson.pop('fechaHoraPago'))
        items = list(map(
            lambda changoXprod: {
                'producto': changoXprod.producto.nombre, 
                'unidad': Producto.objects.get_subclass(pk=changoXprod.producto.pk).unidad,
                'cantidad': changoXprod.cantidad.__str__(),
                'precio': changoXprod.precio.__str__(),
                'id_prod': changoXprod.producto.pk
                },
            carrito.getItems()
            ))
        dictJson['items'] = items
        dictJson['dias_desde_ultima_compra'] = Venta._diasDesdeUltimaCompra(carrito)
        dictJson['total'] = carrito.total().__str__()
        dictJson['nombre_usuario'] = carrito.usuario.first_name
        dictJson['apellido_usuario'] = carrito.usuario.last_name

        print(json.dumps(dictJson))

        return json.dumps(dictJson)

    @staticmethod
    def _diasDesdeUltimaCompra(carrito):
        return diferenciaDias(
            carrito.fechaHoraPago,
            carrito.fechaHoraCreacion
        )

def diferenciaDias(f1, f2):
    return abs(f1 - f2).days

def formatearFechaYHora(fecha):
    return fecha.strftime('%d/%m/%Y %H:%M:%S')