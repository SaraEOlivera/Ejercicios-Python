"""
Realizar la carga de dos números por teclado e imprimir la división del primero respecto al 
segundo, capturar la excepción ZeroDivisionError.

"""

while True:
    try:
        numero1= int(input("Ingrese un numero "))
        numero2= int(input("Ingrese un nuevo numero "))
        division = numero1 / numero2
        print("La division de ambos nros es igual a ", division)
    except ZeroDivisionError:
        print("No se puede dividir un numero por 0")
    