from django.db import models
from productos.models import Producto
from django.conf import settings
from django import User
import django


def prueba():
    # crear usuario:

    usuario = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    # chango:
    chango = Chango(usuario)

    # productos:
    producto1 = Producto(nombre="tomate", precio=200)

    # productos en el chango:


    # falta probar: poder loguearse y que al loguearse te muestre tu carrito y te deje agregar prods ahi.

class Chango(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    fechaCreacion = models.DateTimeField(default=django.utils.timezone.now)
    fechaPago = models.DateTimeField(null=True)
    fuePagado = models.BooleanField(default=False)
        
    def __init__(self, usuario: User):
        self.usuario = usuario
        
    def agregarProducto(self, producto: Producto, cantidad=1):
        if (ChangoXproducto.objects.get(chango=self, producto=producto).exists()):
            self.agregarCantProducto(producto, cantidad)
        else:
            cXp = ChangoXproducto(chango=self, producto=producto, cantidad=cantidad)
            cXp.save()

    def sacarCantProducto(self, producto: Producto, cantidad=1):
        # Validar que este en el carrito?
        cXp = ChangoXproducto.objects.get(chango=self, producto=producto)
        if cXp.cantidad == cantidad:
            cXp.delete()
        else:
            cXp.cantidad -= cantidad
            cXp.save()

    def agregarCantProducto(self, producto: Producto, cantidad=1):
        # Validar que este en el carrito?
        cXp = ChangoXproducto.objects.get(chango=self, producto=producto)
        if cXp.cantidad == cantidad:
            cXp.delete()
        else:
            cXp.cantidad -= cantidad
            cXp.save()
    
    def sacarTodosDeUnProducto(self, producto: Producto):
        # Validar que este en el carrito?
        ChangoXproducto.objects.get(chango=self, producto=producto).delete()
    
    def vaciar(self):
        # Validar que no esté vacio?
        ChangoXproducto.objects.all().filter(chango=self).delete()

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