"""
Almacenar en una tupla los nombres de meses del año. Solicitar el ingreso del número de mes y 
mostrar seguidamente el nombre de dicho mes. Capturar la excepción IndexError.
"""

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
         "Septiembre", "Octubre", "Noviembre", "Diciembre")

try:
    numero = int(input("Ingrese el numero del mes [1 - 12] "))
    if numero > 0:
        print(meses[numero-1])
    else:
        print("El numero no puede ser menor a 1")
except IndexError:
    print("El numero debe ser entre 1 y 12")
