# 1. Implementacion de funcion recursiva
"""
def repetir():
    repetir()

repetir()  # RecursionError

# 2. Implementación de una función recursiva que reciba un parámetro de tipo entero y luego 
# llame en forma recursiva con el valor del parámetro menos 1.

def repetir(x):
    print(x)
    repetir(x-1)

repetir(5)  #RecursionError

# 3. Implementar una función recursiva que imprima en forma descendente de 5 a 1 de uno en uno.

def repetir(x):
    if x > 0:
        print(x)
        repetir(x - 1)

repetir(5)


# 4. Imprimir los números de 1 a 5 en pantalla utilizando recursividad.

def repetir(x):
    if x > 0:
        repetir(x - 1)
        print(x)

repetir(5)



# 5. Obtener el factorial de un número.

def factorial(x):
    if x > 0:
        resultado = x * factorial(x - 1)
        return resultado
    else:
        return 1

#print(f"El factorial de 4 es {factorial(4)}")

def factorial(x):
    if x == 0 or x == 1:
        resultado = 1
    elif x > 1:
        resultado = x * factorial(x - 1)
    return resultado

print(f"El factorial de 4 es {factorial(4)}")

"""

# 6. Implementar un método recursivo para ordenar los elementos de una lista.


def ordenar_lista(lista, cantidad_elementos):
    if cantidad_elementos > 1:
        for f in range(0, cantidad_elementos - 1): #ordena el elem mayor y lo ubica al final
            if lista[f] > lista[f + 1]:
                auxiliar = lista[f]
                lista[f] = lista[f + 1]
                lista[f + 1] = auxiliar
        ordenar_lista(lista, cantidad_elementos - 1)

    
lista = [77, 25, 11, 2, 5]
print(lista)
ordenar_lista(lista, len(lista))
print(lista)

     