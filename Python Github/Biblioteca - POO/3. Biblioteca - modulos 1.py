"""
Desarrollar un programa que cargue una lista con 10 enteros.
Cargar los valores aleatorios con números enteros comprendidos entre 0 y 1000.
Mostrar la lista por pantalla.
Luego mezclar los elementos de la lista y volver a mostrarlo.
"""


import random

def cargarNumeros():
    lista = []
    for x in range(10):
        lista.append(random.randint(0, 1000))
    return lista

def imprimirNumeros(lista):
    print(lista)

def mezclarNumeros(lista):
    random.shuffle(lista)



lista = cargarNumeros()
imprimirNumeros(lista)
mezclarNumeros(lista)
imprimirNumeros(lista)
