import os
from os.path import isfile,join

ruta='D:\curso de python\Datos\python_data\ejercicios_2'

contenido = os.listdir(ruta)
Archivos=[nombre for nombre in contenido if isfile(join(ruta,nombre))]

print(Archivos)