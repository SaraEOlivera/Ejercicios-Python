"""
Confeccionar un módulo que implemente dos funciones, una que retorne el mayor de
dos enteros y otra que retorne el menor de dos enteros.
En el módulo principal importar solo la función que retorne el mayor, luego
cargar dos enteros y mostrar el mayor de ellos
Crear una carpeta llamada proyecto2 y dentro de la misma crear dos módulos
llamados: operacionmayormenor y principal
"""

def calcularMayor(nro1, nro2):
    if nro1 > nro2:
        return nro1
    else:
        return nro2
    



def calcularMenor(nro1, nro2):
    if nro1 < nro2:
        return nro1
    else:
        return nro2
