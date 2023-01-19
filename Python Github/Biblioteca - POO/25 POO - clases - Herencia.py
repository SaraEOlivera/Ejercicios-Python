"""
Declarar una clase Cuenta y dos subclases CajaAhorro y PlazoFijo. Definir los
atributos y métodos comunes entre una caja de ahorro y un plazo fijo y
agruparlos en la clase Cuenta.
Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un
plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer
que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase CajaAhorro y
otro de la clase PlazoFijo.

"""

class Cuenta:

    def __init__(self, titular, monto):
        self.titular = titular
        self.monto = monto

    def imprimir(self):
        print("Titular: ", self.titular)
        print("Saldo disponible ", self.monto)


class CajaAhorro(Cuenta):

    def __init__(self, titular, monto):
        super().__init__(titular, monto)

    def imprimir(self):
        print("Saldo disponible: ")
        super().imprimir()


class PlazoFijo(Cuenta):

    def __init__(self, titular, monto, plazo, intereses):
        super().__init__(titular, monto)
        self.plazo = plazo 
        self.intereses = intereses

    
    def imprimir(self):
        print("Plazo Fijo: ") 
        super().imprimir()
        print("Plazo en días: ", self.plazo)
        print("Intereses: ", self.intereses)
        self.ganancia()

    def ganancia(self):
        ganancia = self.monto * self.intereses / 100
        print("Total con intereses: ", ganancia + self.monto)

#------------------------------------------------------------------

cuenta1 = CajaAhorro("Sara", 70000)
cuenta1.imprimir()

cuenta2 = PlazoFijo("Ana", 45000, 60, 0.75)
cuenta2.imprimir()

    
    
