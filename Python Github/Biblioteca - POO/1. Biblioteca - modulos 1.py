"""
Confeccionar un programa que simule tirar dos dados y luego muestre los valores
que salieron. Imprimir un mensaje que ganó si la suma de los mismos es igual a 7.
"""

import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print("Primer dado: ", dado1)
print("Segundo dado: ", dado2)

suma = dado1 + dado2
if suma == 7:
    print("Gano!")
else:
    print("Perdio")
