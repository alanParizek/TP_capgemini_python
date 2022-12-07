from django.db import models

from pathlib import Path
import sys
from PIL import Image

# cambiar como se hacen los imports en el caso en que rompa
BASE_DIR = str(Path(__file__).resolve().parent.parent)

VDI_DIR = BASE_DIR.removesuffix('listaDeCompras') + 'visualizacionDeImagenes'


sys.path.append(VDI_DIR)
from VDI import * 

sys.path.append(BASE_DIR)

from productos.models import Producto

class ObtenedorDeProductos:
    def __init__(self):
        self.todosLosProductos = Producto.objects.all()
        
    def obtenerProducto(self, img: Image) -> tuple[Producto or None, int or None]:
        visualizacion = VDI()
        nombreProducto = visualizacion.reconocerProducto(img)
        producto = Producto.objects.all().filter(nombre=nombreProducto).select_subclasses().first()


        # en lugar de if(producto.esContable) uso polimorfismo. Si el producto es contable deja cantidad como
        # esta, si no la cambia por None
        # (uso el operador ternario para no hacer producto.cantidad() si no se reconoció el producto
        cantidad = producto.cantidad(visualizacion.contarProductos(img, nombreProducto)) if producto != None else None



        return (producto, cantidad)
