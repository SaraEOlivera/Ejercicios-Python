"""
Implementar la clase Operaciones. Se deben cargar dos valores enteros por
teclado en el método __init__, calcular su suma, resta, multiplicación y
división, cada una en un método, imprimir dichos resultados.
"""

class Operaciones:

    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))

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
primeras.suma()
primeras.resta()
primeras.multiplicacion()
primeras.division()
        
    
