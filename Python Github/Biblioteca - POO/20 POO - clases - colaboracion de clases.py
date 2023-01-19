"""
Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. También el
banco requiere que al final del día calcule la cantidad de dinero que hay
depositado.
"""

class Cliente:

    def __init__(self, nombre): #atributos
        self.nombre = nombre
        self.monto = 0

    def depositar(self, monto): #metodos
        self.monto+= monto

    def extraer(self, monto):
        self.monto-= monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(self.nombre, "Saldo: ", self.monto)


class Banco:

    def __init__(self):
        self.cliente1 = Cliente("Oli")
        self.cliente2 = Cliente("Pepe")
        self.cliente3 = Cliente("Juan")

    def operaciones(self):  #operaciones que se realizan en el dia
        self.cliente1.depositar(300)
        self.cliente1.extraer(78)
        self.cliente2.depositar(10000)
        self.cliente3.depositar(200)

    def ingresos(self):
        depositos = self.cliente1.retornar_monto() + self.cliente2.retornar_monto() + self.cliente3.retornar_monto()
        print("Ingresos del dia: ", depositos)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()


banco1 = Banco()
banco1.operaciones()
banco1.ingresos()
        
    
    

    
        
