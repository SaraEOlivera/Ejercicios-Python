"""
Definir una clase Cliente que almacene un código de cliente y un nombre.
En la clase Cliente definir una variable de clase de tipo lista que almacene 
todos los clientes que tienen suspendidas sus cuentas corrientes.
Imprimir por pantalla todos los datos de clientes y el estado que se encuentra su 
cuenta corriente.

"""

class Cliente:

    suspendidas = []

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
    
    def imprimir(self):
        print("Codigo: ", self.codigo)
        print("Nombre: ", self.nombre)
        self.suspendido()
    

    def suspendido(self):
        if self.codigo in Cliente.suspendidas:
            print("Cliente suspendido")
        else:
            print("Cliente no suspendido")
    
    def suspender(self):
        Cliente.suspendidas.append(self.codigo)


#-----------------------------------------------------------

cliente1 = Cliente(1, "Sara")
cliente2 = Cliente(2, "Sandra")
cliente3 = Cliente(3, "Ana")
cliente4 = Cliente(4, "Ema")
cliente5 = Cliente(5, "Lara")
cliente6 = Cliente(6, "Laura")
cliente7 = Cliente(7, "Sienna")
cliente8 = Cliente(8, "Zara")

cliente6.suspender()
cliente4.suspender()
cliente7.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()
cliente5.imprimir()
cliente6.imprimir()
cliente7.imprimir()
cliente8.imprimir()

print(Cliente.suspendidas)



