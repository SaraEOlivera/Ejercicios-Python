"""
Confeccionar una aplicación que permita cargar por teclado una lista de enteros,
obtener y mostrar el mayor y calcular su suma. Definir un módulo con las
funciones de carga, identificar el mayor y sumar. En el módulo principal del
programa importar el otro módulo y llamar a sus funciones.
"""

def cargarNumeros():
    lista = []
    for x in range(5):
        valor = int(input("Ingrese un valor "))
        lista.append(valor)
    return lista


def calcularMayor(lista):
    mayor = lista[0]
    for x in range(1, 5):
        if lista[x] > mayor:
            mayor = lista[x]
    print(f"El numero mayor de la lista es {mayor}")


def calcularSuma(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    print(f"La suma de los valores de la lista es igual a {suma}")


