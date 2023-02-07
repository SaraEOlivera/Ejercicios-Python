#Captura de todas las excepciones sin discriminar el tipo.
"""
Realizar la carga de dos números por teclado e imprimir la división del primero respecto al 
segundo. Capturar cualquier tipo de excepción que se dispare.
"""

try:
    numero1= int(input("Ingrese un numero "))
    numero2= int(input("Ingrese un nuevo numero "))
    division = numero1 / numero2
    print("La division de ambos numeros es ", division)
except:
    print("Problemas con la entrada de valores o en la operacion")