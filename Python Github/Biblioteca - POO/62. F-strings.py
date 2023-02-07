#Ingresar por teclado dos enteros, calcular su suma y luego mostrar un 
# mensaje de los dos valores ingresados y su suma.

numero1 = int(input("Ingrese un valor "))
numero2 = int(input("Ingrese un valor "))
suma= numero1 + numero2
print(f"La suma de {numero1} y {numero2} es igual a {suma}")
print()
print("---------------------------------------------------------")
print()

#Definir una lista con 5 valores enteros. Mostrar los 5 valores formateados a derecha 
# junto a su suma.

lista= [411, 7, 25, 77, 2, 11, 2012, 103]

for numero in lista:
    print(f"{numero:10}")
print(F"{sum(lista):10}")
print()
print("---------------------------------------------------------")
print()

#Definir una lista con 5 valores flotantes con distintas cantidades de decimales. 
# Mostrar los números solo con dos decimales.

lista_float = [7.777777, 2.500, 2.005, 5.020, 2.1077]

for numero in lista_float:
    print(f"numeros flotantes {numero:10.2f}")
print()
print("---------------------------------------------------------")
print()

#Utilizar los f-strings para cadenas de múltiples líneas:

valor1=77
valor2=34
suma=valor1+valor2
cadena = F"""
         {valor1:9}
         {valor2:9}
         ----------
         {suma:9}   
"""
print(cadena)



