"""
Implementar una clase llamada Alumno que tenga como atributos su nombre y su
nota. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar
un mensaje si está regular (nota mayor o igual a 4)
Definir dos objetos de la clase Alumno.
"""

class Alumno:

    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota ", self.nota)

    def condicion(self):
        if self.nota >= 4:
            print(self.nombre, " Regular")
        else:
            print(self.nombre, "Libre")

#-----------------------------------------------


alumno1 = Alumno()
alumno1.inicializar("Oli", 9)
alumno1.imprimir()
alumno1.condicion()


alumno2 = Alumno()
alumno2.inicializar("Manteca", 8)
alumno2.imprimir()
alumno2.condicion()

alumno3 = Alumno()
alumno3.inicializar("Ana", 3)
alumno3.imprimir()
alumno3.condicion()
    
