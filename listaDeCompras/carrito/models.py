from django.db import models
from productos.models import Producto
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now


class Chango(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    fechaCreacion = models.DateTimeField(default=now)
    fechaPago = models.DateTimeField(null=True)
    fuePagado = models.BooleanField(default=False)
        
    def __init__(self, usuario: User, *args, **kwargs):
        super(Chango, self).__init__(*args, **kwargs)
        self.usuario = usuario
        
    def agregarProducto(self, producto: Producto, cantidad=1):
        try:
            cXp = ChangoXproducto.objects.get(chango=self, producto=producto)
        except ChangoXproducto.DoesNotExist:
            cXp = ChangoXproducto(chango=self, producto=producto, cantidad=0)
        cXp.cantidad += cantidad
        cXp.save()
    
    def sacarTodosDeUnProducto(self, producto: Producto):
        # Validar que este en el carrito?
        ChangoXproducto.objects.get(chango=self, producto=producto).delete()
    
    def cerrarCompra(self):
        self.fechaPago = now()
        self.fuePagado = True
        self.save()

    @staticmethod
    def carritoDelUsuario(usuario):
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
    cantidad = models.IntegerField()