"""
Plantear una clase Rectangulo. Definir dos atributos (ladomenor y ladomayor). Redefinir el 
operador == de tal forma que tengan en cuenta la superficie del rectángulo. Lo mismo hacer con 
todos los otros operadores relacionales.

"""

class Rectangulo:

    def __init__(self, lado_menor, lado_mayor):
        self.lado_menor = lado_menor
        self.lado_mayor = lado_mayor
    
    def calcular_superficie(self):
        return self.lado_menor * self.lado_mayor
    
    def __ne__(self, object2):
        if self.calcular_superficie() != object2.calcular_superficie():
            return True
        else:
            return False


#-----------------------------------------------------------------------------

rectangulo1 = Rectangulo(44, 106)
rectangulo2 = Rectangulo(4, 16)
if rectangulo1 != rectangulo2:
    print("Los rectangulos tienen diferente superficie")

    

