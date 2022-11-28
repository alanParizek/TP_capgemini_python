from django.db import models

from pathlib import Path
import sys

BASE_DIR = str(Path(__file__).resolve().parent.parent)

VDI_DIR = BASE_DIR.removesuffix('listaDeCompras') + 'visualizacionDeImagenes'

DB_DIR = BASE_DIR + '\productos'

sys.path.append(VDI_DIR)
from VDI import * 



#from productos.models import Producto

class obtenedorDeProductos:
    def __init__(self):
        
        self.ID_productos = {

        }

    def obtenerProducto(self, imgPath):
        visualizacion = VDI()
        return visualizacion.visualizarImagen(imgPath)


        
        



