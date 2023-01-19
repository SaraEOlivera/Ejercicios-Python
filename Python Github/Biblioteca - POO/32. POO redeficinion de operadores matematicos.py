"""
Desarrollar una clase llamada Lista, que permita pasar al método 
__init__ una lista de valores enteros.
Redefinir los operadores +,-,* y // con respecto a un valor entero.
"""

class Lista:
    
    def __init__(self, valores):
        self.valores = valores
    
    def imprimir(self):
        print(self.valores)
    
    def __add__(self, entero):
        resultado = []
        for x in range(len(self.valores)):
            resultado.append(self.valores[x] + entero)
        return resultado

    def __sub__(self, sub_entero):
        resultado = []
        for x in range(len(self.valores)):
            resultado.append(self.valores[x] - sub_entero)
        return resultado
    
    def __mul__(self, mul_entero):
        resultado = []
        for x in range(len(self.valores)):
            resultado.append(self.valores[x] * mul_entero)
        return resultado

    def __floordiv__(self, floor_entero):
        resultado = []
        for x in range(len(self.valores)):
            resultado.append(self.valores[x] // floor_entero)
        return resultado

#----------------------------------------------------------

lista1 = Lista([1, 2, 3, 4])
print("Lista original")
lista1.imprimir()
print("Lista nueva")
print(lista1 + 7)
print("-----------------------------")
lista1 = Lista([10, 20, 30, 40])
print("Lista original")
lista1.imprimir()
print("Lista nueva")
print(lista1 - 5)
print("-----------------------------")
lista1 = Lista([5, 10, 20, 30])
print("Lista original")
lista1.imprimir()
print("Lista nueva")
print(lista1 * 2)
print("-----------------------------")
lista1 = Lista([50, 40, 30, 20])
print("Lista original")
lista1.imprimir()
print("Lista nueva")
print(lista1 // 5)

