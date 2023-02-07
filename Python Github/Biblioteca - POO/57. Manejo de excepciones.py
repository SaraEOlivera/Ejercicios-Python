#Captura de múltiples excepciones con un try.

"""
Realizar la carga de dos números por teclado e imprimir la división del primero respecto al 
segundo, capturar las excepciones ZeroDivisionError y ValueError.
"""

try:
    numero1= int(input("Ingrese un numero "))
    numero2= int(input("Ingrese un nuevo numero "))
    division = numero1 / numero2
    print("La division de ambos numeros es ", division)
except ZeroDivisionError:
    print("Mo se puede dividir por 0")
except ValueError:
    print("Debe ingresar un numero ")