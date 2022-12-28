"""
Implementaremos una clase llamada Persona que tendrá como atributo (variable)
su nombre y dos métodos (funciones), uno de dichos métodos inicializará el
atributo nombre y el siguiente método mostrará en la pantalla el contenido del
mismo.
Definir dos objetos de la clase Persona.
"""

#Declaracion de clase y definicion de metodos:

class Persona:
    #parametro 1 siempre self, la referencia del objto
    def inicializar(self, nomb):
        self.nombre = nomb
        #identificador self + nombre atributo. guardar el parametro
        #Este metodo queda encapsulado en la class persona. cualquier metodo puede usarlo

    def imprimir(self):
        print("Nombre: ", self.nombre) #c/self se accede al atributo nombre

#---------------------------------------------------------------

#Sintaxis para crear objetos de la clase persona
#Aqui no se usa self solo se usa al declarar metodos. Self guarda referencia del objeto

persona1 = Persona()
persona1.inicializar("Oli")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Manteca")
persona2.imprimir()
    
