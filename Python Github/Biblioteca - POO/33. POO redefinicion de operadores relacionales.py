"""
Crear una clase Persona que tenga como atributo el nombre y la edad.
El operador == retornará verdadero si las dos personas tienen la misma edad, el 
operador > retornará True si la edad del objeto de la izquierda tiene una edad mayor a la edad 
del objeto de la derecha del operador >, y así sucesivamente

"""

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self,objeto2):
        if self.edad == objeto2.edad:
            return True
        else:
            return False
    
    def __gt__(self,objeto2):
        if self.edad > objeto2.edad:
            return True
        else:
            return False
    



#-------------------------------------------------

p1 = Persona("Sara", 10)
p2 = Persona("Ariel", 4)

if p1 > p2:
     print("P1 es mayor que p2")
else:
    print("p2 es mayot")
    