"""
Confeccionar una clase que permita carga el nombre y la edad de una persona.
Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)
"""


class Persona:

    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

    def calcular_mayoria(self):
        if self.edad >= 18:
            print(self.nombre, " es mayor de edad")
        else:
            print(self.nombre, " es menor de edad")

#----------------------------------------------------------


persona1 = Persona()
persona1.inicializar("Luis", 4)
persona1.imprimir()
persona1.calcular_mayoria()


persona2 = Persona()
persona2.inicializar("Juana", 34)
persona2.imprimir()
persona2.calcular_mayoria()


persona3 = Persona()
persona3.inicializar("Emma", 44)
persona3.imprimir()
persona3.calcular_mayoria()
