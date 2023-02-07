"""
Realizar la carga de dos números enteros por teclado e imprimir su suma, luego preguntar si 
quiere seguir sumando valores.
Codificar dos programas uno que capture la excepción de ingreso de datos no numéricos y el otro 
que no tenga en cuenta el tipo de entrada de datos.
"""
""" while True:
    numero1=int(input("Ingrese un numero "))
    numero2=int(input("Ingrese un nuevo numero "))
    suma=numero1+numero2
    print("suma:", suma)
    rpta= input("Desea ingrear otro numero? S / N ")
    if rpta == "N":
        break """

#----------------- con exepciones:
while True:
    try:
        numero1=int(input("Ingrese un numero "))
        numero2=int(input("Ingrese un nuevo numero "))
        suma=numero1+numero2
        print("suma:", suma)
    except ValueError:
        print("Debe ingresar un numero")
    rpta= input("Desea ingresar otro numero? [s / n] ")
    if rpta == "n":
        break
        
    