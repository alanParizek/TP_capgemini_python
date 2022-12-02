from django.db import models

from pathlib import Path
import sys

BASE_DIR = str(Path(__file__).resolve().parent.parent)

VDI_DIR = BASE_DIR.removesuffix('listaDeCompras') + 'visualizacionDeImagenes'


sys.path.append(VDI_DIR)
from VDI import * 

sys.path.append(BASE_DIR)

from productos.models import Producto

class obtenedorDeProductos:
    def __init__(self):

        self.todosLosProductos = Producto.objects.all()
        self.ID_productos = {

        }
        for i in self.todosLosProductos:
            self.ID_productos.update({self.todosLosProductos[i] : i})
        

    def obtenerProducto(self, imgPath):
        visualizacion = VDI()
        producto = visualizacion.visualizarImagen(imgPath)[0]
        cantidad = visualizacion.visualizarImagen(imgPath)[0]
        listaProductos = self.ID_productos.keys()
        for item in listaProductos:
            if producto == -1:
                resultado = -1    
            elif item == producto:
                resultado = self.ID_productos.get(item)

        return (resultado, cantidad)


        
        



