import os
from os.path import isfile,join

ruta='D:\curso de python\Datos\python_data\ejercicios_2'

#for i in os.scandir(path):
#    print(i,"=",i.path)
#    print(i.is_dir())
def listarcarpeta(rut):
    
    contenido = os.listdir(rut)
    Archivos=[nombre for nombre in contenido if isfile(join(rut,nombre))]

listarcarpeta(ruta)