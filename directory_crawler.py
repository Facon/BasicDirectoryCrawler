# -*- coding: cp1252 -*-

###############
#Plataforma: Windows
#Fecha: 14/05/2009
#Descripcion: Recorre la unidad actual de la cual se ejecuta el programa
#y guarda la ruta del fichero en el archivo listado.txt
###############
import string
import os
 
directorio = os.getcwd()
lista = directorio
 
f = open('listado.txt', 'w')
 
directorio = directorio.split("\\")
directorio = directorio[0]
 
os.chdir(directorio + os.path.sep)
 
 
def listado(dir):
    for file in os.listdir(dir):
        archivo = dir + os.path.sep + file
        if os.path.isfile(archivo):
            f.write(archivo+"\n")
        else:
            listado(archivo)
 
listado(directorio)
 
f.close()
