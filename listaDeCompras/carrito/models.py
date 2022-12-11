from django.core.validators import MinValueValidator
from django.db import models
from productos.models import Producto
from django.conf import settings
from django.contrib.auth.models import User
from ventas.models import Venta
from datetime import datetime as dt

class Chango(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    fechaHoraCreacion = models.DateTimeField(default=dt.now())
    fechaHoraCierre = models.DateTimeField(null=True)
    @property
    def estaAbierto(self):
        return self.fechaHoraCierre is None

    def validarPuedeModificarse(self):
        if not self.estaAbierto:
            raise NoPuedeModificarseException('No se puede modificar un carrito cerrado')

    def agregarProducto(self, producto: Producto, cantidad=1):
        self.validarPuedeModificarse()
        try:
            cXp = ChangoXproducto.objects.get(chango=self, producto=producto)
        except ChangoXproducto.DoesNotExist:
            cXp = ChangoXproducto(chango=self, producto=producto, cantidad=0)
        cXp.cantidad += cantidad
        cXp.desnormalizarPrecio()
        cXp.save()
    
    def sacarTodosDeUnProducto(self, producto: Producto):
        self.validarPuedeModificarse()
        ChangoXproducto.objects.get(chango=self, producto=producto).delete()
    
    def cerrarCompra(self):
        self.validarPuedeModificarse()
        self._validarPuedeCerrarse()
        self.fechaHoraCierre = dt.now()
        Venta.registrarVenta(self)
        self.save()

    def total(self):
        return sum(map(lambda cXp: cXp.precio, ChangoXproducto.objects.filter(chango=self)))

    def getItems(self):
        return ChangoXproducto.objects.filter(chango=self)

    def _validarPuedeCerrarse(self):
        if self.noTieneProductos():
            raise NoPuedeCerrarseLaCompraException('Antes de cerrar la compra debe seleccionar los productos')

    def noTieneProductos(self):
        return self.getItems().count() <= 0
    
    def diasDesdeUltimaCompra(self):
        return diferenciaDias(
            self.fechaHoraCierre,
            self.fechaHoraCreacion
        )

    @staticmethod
    def carritoDelUsuario(usuario: User):
        return Chango.objects.get(usuario=usuario, fechaHoraCierre=None)

class ChangoXproducto(models.Model):
    chango = models.ForeignKey(
        'carrito.Chango',
        on_delete=models.CASCADE,
        )
    producto = models.ForeignKey(
        'productos.Producto',
        on_delete=models.CASCADE,
        )
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    precio = models.DecimalField(max_digits=25, decimal_places=2, validators=[MinValueValidator(0)])

    def desnormalizarPrecio(self) -> None:
        producto = Producto.objects.get_subclass(pk=self.producto_id)
        self.precio = producto.precioRedondeado(self.cantidad)
    
    def __str__(self):
        return self.producto.__str__()
    
def diferenciaDias(f1, f2):
    return abs(f1 - f2).days

class NoPuedeCerrarseLaCompraException(Exception):
    pass

class NoPuedeModificarseException(Exception):
    pass