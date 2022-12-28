"""
Desarrollar una clase que represente un punto en el plano y tenga los siguientes
métodos: inicializar los valores de x e y que llegan como parámetros, imprimir
en que cuadrante se encuentra dicho punto (concepto matemático, primer cuadrante
si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)
"""

class Punto:

    def __init__(self):
        self.x = int(input("Ingrese el punto x: "))
        self.y = int(input("Ingrese el punto y: "))

    def imprimir(self):
        if self.x > 0 and self.y > 0:
            print("Primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print("Segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print("Tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            print("Cuarto cuadrante")



#----------------------------------------------------------

punto1 = Punto()
punto1.imprimir()
