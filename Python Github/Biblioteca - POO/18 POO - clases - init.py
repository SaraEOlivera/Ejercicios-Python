"""
Plantear una clase que administre dos listas de 5 nombres de alumnos y sus
notas. Mostrar un menú de opciones que permita:
1- Cargar alumnos.
2- Listar alumnos.
3- Mostrar alumnos con notas mayores o iguales a 7.
4- Finalizar programa.
"""

class Alumnos:
    
    def __init__(self):
        self.nombres = []
        self.notas = []

    def menu(self):
        opcion = 0
        print("Bienvenido. Observe las opciones")
        while opcion != 5:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Mostrar alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion = int(input("¿Que desea realizar? "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.notas_altas()
            elif opcion == 4:
                print("Programa finalizado")
                break
                
    def cargar(self):
        for x in range(5):
            nombre = input("Ingrese el nombre del alumno: ")
            self.nombres.append(nombre)
            nota = int(input("Ingrese la nota del alumno: "))
            self.notas.append(nota)

    def listar(self):
        print("Listado de alumnos y sus correspondientes notas")
        for x in range(5):
            print(self.nombres[x], self.notas[x])

    def notas_altas(self):
        print("Alumnos con notas altas")
        for x in range(5):
            if self.notas[x]>= 7:
                print(self.nombres[x], self.notas[x])


#------------------------------------------------------------------

grupo1 = Alumnos()
grupo1.menu()
        
            
