"""
Veamos con un ejemplo la sintaxis para redefinir el operador +.
Crearemos una clase Cliente de un banco y redefiniremos el operador + 
para que nos retorne la suma de los depósitos de los dos clientes que 
estamos sumando
"""

class Cliente:

    def __init__(self, nombre, monto):
        self.nombre = nombre
        self.monto = monto
    
    def __add__(self, objeto2):
        suma = self.monto + objeto2.monto
        return suma

#-----------------------------------------------------

cliente1 = Cliente("Juan", 500)
cliente2 = Cliente("Juana", 5200)

print("Total depositos:")
print(cliente1 + cliente2)
