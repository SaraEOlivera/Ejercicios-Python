"""
Desarrollar un programa que cargue los lados de un triángulo e implemente los
siguientes métodos: inicializar los atributos, imprimir el valor del lado mayor
y otro método que muestre si es equilátero o no. El nombre de la clase llamarla
Triangulo.
"""

class Triangulo:

    def inicializar(self):
        self.lado1 = int(input("Ingrese el lado1: "))
        self.lado2 = int(input("Ingrese el lado1: "))
        self.lado3 = int(input("Ingrese el lado1: "))

    def imprimir_lado_mayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El lado mayor es ", self.lado3)
        else:
            if self.lado2 > self.lado3:
                print("El lado mayor es ", self.lado2)
            else:
                print("El lado mayor es ", self.lado3)

    def calcular_equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Triangulo equilatero")
        else:
            print("No es un triangulo equilatero")

#------------------------------------------------------------


triangulo1 = Triangulo()
triangulo1.inicializar()
triangulo1.imprimir_lado_mayor()
triangulo1.calcular_equilatero()

triangulo2 = Triangulo()
triangulo2.inicializar()
triangulo2.imprimir_lado_mayor()
triangulo2.calcular_equilatero()

triangulo3 = Triangulo()
triangulo3.inicializar()
triangulo3.imprimir_lado_mayor()
triangulo3.calcular_equilatero()
