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
        
    def obtenerProducto(self, img: Image):
        visualizacion = VDI()
        nombreProducto = visualizacion.reconocerProducto(img)
        # validar que exista un producto con ese nombre?
        producto = Producto.objects.all().filter(nombre=nombreProducto).first()
        cantidad = 4
        
        return (producto, cantidad)
