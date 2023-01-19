"""
Declarar una clase llamada Familia. Definir como atributos el nombre del 
padre, madre y una lista con los nombres de los hijos.
Definir el método especial __str__ que retorne un string con el nombre 
del padre, la madre y de todos sus hijos.
"""
class Familia:

    def __init__(self, nombre_padre, nombre_madre, hijos = []):
        self.nombre_padre = nombre_padre
        self.nombre_madre = nombre_madre
        self.hijos = hijos
    
    def __str__(self):
            flia = f'{self.nombre_padre};{self.nombre_madre};'
            for hijo in self.hijos:
                flia = flia + hijo + ' '
            return flia

#--------------------------------------------------------------



flia1 = Familia('Mario', 'Lucia', ['Laura', 'Pedro', 'Juan'])
flia2 = Familia('Juan', 'Nara', ['Lia', 'Gabriela'])
flia3 = Familia('Mauro', 'Lara', ['Luana'])
flia4 = Familia("Ruben", "Valera")

print(flia1)
print(flia2)
print(flia3)
print(flia4)

