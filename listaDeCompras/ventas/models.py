from django.db import models
from datetime import datetime
from django.conf import settings
import json
from productos.models import Producto
# Create your models here.


class Venta(models.Model):    
    carrito = models.ForeignKey(
        'carrito.Chango',
        null=True,
        on_delete=models.SET_NULL,
        )
    fechaHoraPago = models.DateTimeField(null=True)
    jsonText = models.TextField()
    
    def cobrar(self):
        self.fechaHoraPago = datetime.now()
        self.guardarJson()
        self.save()

    def guardarJson(self):
        self.jsonText = self.crearTextoJson()
    
    def crearTextoJson(self) -> str:
        carrito = self.carrito
        dictJson = carrito.__dict__.copy()
        dictJson['idCarrito'] = dictJson.pop('id') #Cambiando nombre a la key id del carrito
        dictJson.pop('_state')
        dictJson.pop('fechaHoraCreacion')
        dictJson['fecha_hora_cierre_carrito'] = formatearFechaYHora(dictJson.pop('fechaHoraCierre'))
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
        dictJson['dias_desde_ultima_compra'] = carrito.diasDesdeUltimaCompra()
        dictJson['total'] = carrito.total().__str__()
        dictJson['nombre_usuario'] = carrito.usuario.first_name
        dictJson['apellido_usuario'] = carrito.usuario.last_name
        return json.dumps(dictJson)
    
    @staticmethod
    def registrarVenta(carrito):
        venta = Venta(carrito=carrito)
        venta.save()
        # arma la venta con el carrito y la guarda en la DB

    @staticmethod
    def pendientesDePago():
        return Venta.objects.filter(fechaHoraPago=None)

def formatearFechaYHora(fecha):
    return fecha.strftime('%d/%m/%Y %H:%M:%S')