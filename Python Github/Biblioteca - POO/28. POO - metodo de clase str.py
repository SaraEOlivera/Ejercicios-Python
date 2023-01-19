"""
Definir una clase llamada Punto con dos atributos x e y.
Crearle el método especial __str__ para retornar un string con 
el formato (x,y).
"""

class Punto:

    def __init__(self, x, y):
        self.y = y
        self.x = x
    
    def __str__(self):
        coordenadas = f'({self.y} y {self.x})'
        return coordenadas

#---------------------------------------------------

punto1 = Punto(4, 7)
punto2 = Punto(-8, 12)
print(punto1)
print(punto2)