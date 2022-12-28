"""
Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos:
inicializar el valor del lado llegando como parámetro al método __init__
(definir un atributo llamado lado), imprimir su perímetro y su superficie.
"""

class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        perimetro = self.lado * 4
        print("Perímetro: ", perimetro)

    def superficie(self):
        superficie = self.lado * self.lado
        print("Superficie: ", superficie)

#--------------------------------------------------------

cuadrado1 = Cuadrado(10)
cuadrado1.perimetro()
cuadrado1.superficie()
        
