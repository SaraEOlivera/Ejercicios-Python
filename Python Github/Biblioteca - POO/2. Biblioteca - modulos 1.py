import random
""" Confeccionar un programa que genere un número aleatorio entre 1 y 100 y n
se muestre.
El operador debe tratar de adivinar el número ingresado.
Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al
generado o "El número aleatorio es mayor" o "El número aleatorio es menor".
Mostrar cuando gana el jugador cuantos intentos necesitó"""



print("*******************")
print("Adivine el número")
print("*******************")
print()

numeroAleatorio = random.randint(1, 30)
cantidadIntentos = 0
numeroElegido = -1

while numeroElegido != numeroAleatorio:
    numeroElegido = int(input("Ingrese un numero entre 1 y 100: "))
    if numeroAleatorio > numeroElegido:
        print("El numero ingresado es mayor")
    elif numeroAleatorio < numeroElegido:
        print("El número ingresado es menor")
    cantidadIntentos += 1
print("Gano en ", cantidadIntentos, " intentos")
