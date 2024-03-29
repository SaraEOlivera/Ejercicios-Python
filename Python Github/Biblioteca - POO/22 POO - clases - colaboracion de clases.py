"""
Pantear una clase Club y otra clase Socio
La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el
club (en años).
En el método __init__ de la clase Socio pedir la carga por teclado del nombre y
su antigüedad.
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor
antigüedad en el club.
"""

class Socio:

    def __init__(self):
        self.nombre = input("Ingrese el nombre del socio ")
        self.antiguedad = int(input("Ingrese la antiguedad del socio "))
        

    def retornar_antiguedad(self):
        return self.antiguedad

    def imprimir_antiguedad(self):
        print("Socio más antiguo ", self.nombre, "con ", self.antiguedad, " años de antigüedad")
        
        
class Club:

    def __init__(self):
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()


    def socio_antiguo(self):
        if (self.socio1.retornar_antiguedad() > self.socio2.retornar_antiguedad() and
            self.socio1.retornar_antiguedad() > self.socio3.retornar_antiguedad()):
            self.socio1.imprimir_antiguedad()
        elif self.socio2.retornar_antiguedad() > self.socio3.retornar_antiguedad():
            self.socio2.imprimir_antiguedad()
        else:
            self.socio3.imprimir_antiguedad()

socios = Club()
socios.socio_antiguo()
        
