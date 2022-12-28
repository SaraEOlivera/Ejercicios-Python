"""
Confeccionar un programa que solicite la carga de un valor entero por teclado
y luego nos muestre la raíz cuadrada del número y el valor elevado al cubo.



from math import pow, sqrt

valor = int(input("Ingrese un valor "))
cubo = pow(valor, 3)
raiz = sqrt(valor)

print(f"El valor elevado al cubo de {valor} es igual a {cubo}")
print(f"La raiz de {valor} es igual a {raiz}")

"""


#Repetir ejercicio utilizando alias

from math import pow as cubo, sqrt as raiz

valor = int(input("Ingrese un valor "))
cube = cubo(valor, 3)
raiz = raiz(valor)

print(f"El valor elevado al cubo de {valor} es igual a {cube}")
print(f"La raiz de {valor} es igual a {raiz}")
