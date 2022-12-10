from django.core.validators import MinValueValidator
from django.db import models
from productos.models import Producto
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now
from ventas.models import Venta

class Chango(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    fechaHoraCreacion = models.DateTimeField(default=now)
    fechaHoraPago = models.DateTimeField(null=True)
    fuePagado = models.BooleanField(default=False)
        
    def agregarProducto(self, producto: Producto, cantidad=1):
        try:
            cXp = ChangoXproducto.objects.get(chango=self, producto=producto)
        except ChangoXproducto.DoesNotExist:
            cXp = ChangoXproducto(chango=self, producto=producto, cantidad=0)
        cXp.cantidad += cantidad
        cXp.desnormalizarPrecio()
        cXp.save()
    
    def sacarTodosDeUnProducto(self, producto: Producto):
        # Validar que este en el carrito?
        ChangoXproducto.objects.get(chango=self, producto=producto).delete()
    
    def cerrarCompra(self):
        self._validarPuedeCerrarse()
        self.fechaHoraPago = now()
        self.fuePagado = True
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

    @staticmethod
    def carritoDelUsuario(usuario: User):
        return Chango.objects.get(usuario=usuario, fuePagado=False)

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

class NoPuedeCerrarseLaCompraException(Exception):
    pass