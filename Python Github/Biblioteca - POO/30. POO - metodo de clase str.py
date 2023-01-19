"""
Desarrollar un programa que implemente una clase llamada Jugador.
Definir como atributos su nombre y puntaje.
Codificar el método especial __str__ que retorne el nombre y si es principiante 
(menos de 1000 puntos) o experto (1000 o más puntos)
"""

class Jugador:

    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
    
    def __str__(self):
        if self.puntaje < 1000:
            jugador = f'{self.nombre}  es un jugador principiante'
            return jugador
        else:
            jugador = f'{self.nombre} es un jugador experto'
            return jugador

#------------------------------------------------------

jugador1 = Jugador("Raul", 1400)
jugador2 = Jugador("Amelia", 900)

print(jugador1)
print(jugador2)