from pathlib import Path
import os
import cv2
import numpy as np

BASE_DIR = str(Path(__file__).resolve().parent.parent)

BANANA = 46
MANZANA = 47
BROCOLI = 50

BANANA_CANNY = (51,320,10)
MANZANA_CANNY = (51,350,10)

BROCCOLI_DEF_QTY = 1

PRODUCTOS = (BANANA, MANZANA, BROCOLI)


class VDI:
    def __init__(self):
        self.net = cv2.dnn.readNet(BASE_DIR + "/visualizacionDeImagenes/yolov4/yolov4.weights", BASE_DIR + "/visualizacionDeImagenes/yolov4/yolov4.cfg")
        self.model= cv2.dnn_DetectionModel(self.net)
        self.model.setInputParams(size=(320,320), scale=1/255)
        self.clases=[]
        with open(BASE_DIR + "/visualizacionDeImagenes/yolov4/classes.txt") as objeto_archivo:
            for nombre_clase in objeto_archivo.readlines():
                nombre_clase=nombre_clase.strip()
                self.clases.append(nombre_clase)

    def visualizarImagen(self, imgPath):
        cantidad = BROCCOLI_DEF_QTY
        img = cv2.imread(imgPath)
        producto = self.reconocerProducto(img)
        if producto != 'brocoli':
            cantidad = self.contarProductos(img, producto)
        resultado = [producto, cantidad]
        return resultado

    def reconocerProducto(self, img):
        resultados = ''
        (id_clase, puntaje, caja)=self.model.detect(img)
        for id_clase, puntaje, caja in zip(id_clase, puntaje, caja):
            for producto in PRODUCTOS:
                if id_clase == producto:
                    resultados = self.clases[id_clase]
        if resultados == '':
            resultados = -1
        return resultados

    def contarProductos(self, img, producto):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (11, 11), 0)

        if producto == 'manzana':
            canny = cv2.Canny(blur, MANZANA_CANNY[0],MANZANA_CANNY[1],MANZANA_CANNY[2])
        else:
            canny = cv2.Canny(blur, BANANA_CANNY[0],BANANA_CANNY[1],BANANA_CANNY[2])
 
        dilated = cv2.dilate(canny, (1, 1), iterations=0)
 
        (cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        return len(cnt)


