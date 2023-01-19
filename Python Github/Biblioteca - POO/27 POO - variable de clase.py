"""
Plantear una clase llamada Jugador.
Definir en la clase Jugador los atributos nombre y puntaje, y los métodos __init__, 
imprimir y pasar_tiempo (que debe reducir en uno la variable de clase).
Declarar dentro de la clase Jugador una variable de clase que indique cuantos 
minutos falta para el fin de juego (iniciarla con el valor 30)
Definir en el bloque principal dos objetos de la clase Jugador.
Reducir dicha variable hasta llegar a cero.

"""

class Jugador:
    minutos_para_terminar = 30

    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
    
    def imprimir(self):
        print("Nombre del jugador ", self.nombre)
        print("Puntos logrados ", self.puntaje)
        print("Final del juego: ", Jugador.minutos_para_terminar, " minutos")
    
    def pasar_tiempo(self):
        Jugador.minutos_para_terminar = Jugador.minutos_para_terminar - 1


#----------------------------------------------------

jugador1 = Jugador("Mitre", 50)
jugador2 = Jugador("Oli", 90)

while Jugador.minutos_para_terminar>0:
    jugador1.imprimir()
    jugador2.imprimir()
    jugador1.pasar_tiempo()
