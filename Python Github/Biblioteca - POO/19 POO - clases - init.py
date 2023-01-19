"""
Confeccionar una clase que administre una agenda personal. Se debe almacenar el
nombre de la persona, teléfono y mail. Debe mostrar un menú con estas opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.
"""

class Agenda:

    def __init__(self):
        self.nombres = []
        self.telefonos = []
        self.mails = []
        contactos = 0

    def menu(self):
        opcion = 0
        print("Bienvenido a su agenda. Observe las opciones")
        while opcion != 6:
            print("1- Carga de un contacto en la agenda")
            print("2- Listado completo de la agenda")
            print("3- Consulta ingresando el nombre de la persona")
            print("4- Modificación de su teléfono y mail")
            print("5- Finalizar programa")
            opcion = int(input("¿Qúe desea realizar? "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.consultar()
            elif opcion == 4:
                self.modificar()
            elif opcion == 5:
                print("Ha salido de la agenda")
                break


    def cargar(self):
        self.contactos = int(input("¿Cuantos contactos quiere agregar? "))
        for x in range(self.contactos):
            nombre = input("Ingrese el nombre del contacto ")
            self.nombres.append(nombre)
            tel = input("Ingrese el teléfono del contacto ")
            self.telefonos.append(tel)
            mail = input("Ingrese el mail del contacto ")
            self.mails.append(mail)
        print("---------------------------------------------------------------------")

    def listar(self):
        print("Lista de contactos")
        for x in range(self.contactos):
            print(self.nombres[x], self.telefonos[x], self.mails[x])
        print("---------------------------------------------------------------------")

    def consultar(self):
        consulta = input("Ingrese el nombre de la persona ")
        for x in range(self.contactos):
            if consulta == self.nombres[x]:
                print(self.nombres[x], self.telefonos[x], self.mails[x])
            elif consulta != self.nombres[x]:
                print("El nombre no está registrado")
        print("---------------------------------------------------------------------")

    def modificar(self):
        encontrado = False
        consulta = input("Ingrese el nombre del contacto a modificar ")
        for x in range(self.contactos):
            if consulta == self.nombres[x]:
                pregunta = input("¿Desea modificar el mail, el telefono o ambos? M / T / A ")
                if pregunta == "T":
                    modificacion_tel = int(input("Ingrese el nuevo telefono "))
                    self.telefonos[x] = modificacion_tel
                    print("El telefono fue moficado")
                elif pregunta == "M":
                    modificacion_mail = input("Ingrese el nuevo mail ")
                    self.mails[x] = modificacion_mail
                    print("El mail fue moficado")
                elif pregunta == "A":
                    modificacion_tel = int(input("Ingrese el nuevo telefono "))
                    self.telefonos[x] = modificacion_tel
                    modificacion_mail = input("Ingrese el nuevo mail ")
                    self.mails[x] = modificacion_mail
                    print("Los datos fueron moficados")
                encontrado = True
            if encontrado == False:
                print("El nombre no está registrado")
        print("---------------------------------------------------------------------")


#------------------------------------------------------------------------------

grupo1 = Agenda()
grupo1.menu()
    
