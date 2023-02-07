# Recorrer un árbol de directorios en forma recursiva. Mostrar de cada directorios los archivos 
# y directorios, luego descender a cada directorio y hacer la misma actividad.

import os

def  leer(directorio):
    lista = os.listdir(directorio)
    for elemento in lista:
        if os.path.isfile(directorio+elemento):
            print(elemento+" [archivo]")
        if os.path.isdir(directorio+elemento):
            print(elemento+" [directorio]")
            leer(directorio+elemento+"/")

leer("C:/Users/PICHUS/Documents/OLI/Developer/GitHub/Python - Github/Python Github/Biblioteca - POO/")