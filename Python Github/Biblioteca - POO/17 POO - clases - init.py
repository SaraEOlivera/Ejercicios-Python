"""
Plantear una clase Operaciones que solicite en el método __init__ la carga de
dos enteros e inmediatamente muestre su suma, resta, multiplicación y división.
Hacer cada operación en otro método de la clase Operación y llamarlos desde el
mismo método __init__
"""

class Operaciones:

    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        suma = self.valor1 + self.valor2
        print("suma: ", suma)

    def resta(self):
        resta = self.valor1 - self.valor2
        print("resta: ", resta)

    def multiplicacion(self):
        producto = self.valor1 * self.valor2
        print("producto: ", producto)

    def division(self):
        division = self.valor1 // self.valor2
        print("division: ", division)

#-----------------------------------------------------------------------

primeras = Operaciones()
segundas = Operaciones()

        
