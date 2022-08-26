# 1 Hallar la superficie de un cuadrado conociendo el valor de un lado.

lado = int(input("Ingrese la medida de lado del cuadrado: "))
superficie = lado * lado
print("La superficie del cuadrado es:")
print(superficie)

#----------------------------------------------------
#2 Realizar la carga de dos números enteros por teclado e imprimir su suma y su producto.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
suma = numero1 + numero2
producto = numero1 * numero2
print("El resultado de la suma de ambos numeros es: ", suma)
print("El resultado de la multiplicación de ambos numeros es: ", producto)

#--------------------------------------------------
# 3 Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)

precio = int(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad a llevar: "))
importe = precio * cantidad
print("El importe total es ", importe)

#----------------------------------------------------------
# 4 Realizar la carga del lado de un cuadrado, mostrar por pantalla el perímetro del mismo (El perímetro de un cuadrado se calcula multiplicando el valor del lado por cuatro)

lado = int(input("Ingrese el lado del cuadrado: "))
perimetro = lado * 4
print("El perímetro del cuadrado es ", perimetro)

#------------------------------------------------------------
# 5 Escribir un programa en el cual se ingresen cuatro números, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
num4 = int(input("Ingrese el cuarto numero: "))
suma = num1 + num2
producto = num3 * num4
print("La suma de los dos primeros numeros es: ", suma)
print("El producto de los dos últimos números es: ", producto)

#------------------------------------------------------------------
# 6 Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))
num4 = int(input("Ingrese el cuarto valor: "))
suma = num1 + num2 + num3 + num4
promedio = suma / 4
print("La suma de todos los valores es ", suma)
print("El promedio de estos valores es ", promedio)

#------------------------------------------------------------

# 7 calcular el sueldo mensual de un operario sabiendo las horas trabajadas y el valor por hora

horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
valor_hora = int(input("Ingrese el valor por hora: "))
sueldo = valor_hora * horas_trabajadas
print("El sueldo del operario es ", sueldo)

#----------------------------------------------------------------

# 8 Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos.

sueldo = int(input("Ingrese el sueldo en dolares del empleado: "))
if sueldo > 3000:
    print("Debe pagar impuestos")

#-------------------------------------------------------

#  9: Realizar un programa que solicite ingresar dos números distintos y muestre por pantalla el mayor de ellos.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
# este print no forma parte de la estructura condicional.
print("El valor mayor es:")
if num1 > num2:
    print(num1)
else:
    print(num2,)

#------------------------------------------------------------------------

# 10 Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo.

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
if num1 > num2:
    suma = num1 + num2
    diferencia = num1 - num2
    print("La suma de ambos valores es ", suma)
    print("La diferencia entre ambos valores es ", diferencia)
else:
    producto = num1 * num2
    division = num1 / num2
    print("El producto entre ambos valores es ", producto)
    print("La división entre el primer valor sobre el segundo es ", division)

#-----------------------------------------------------------------

""" #11 Se ingresan tres notas de un alumno,
#si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado" """

nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 7:
    print("Promocionado")

#------------------------------------------------------------

""" # 12 Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos. Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)"""

numero = int(input("Ingrese un numero entre 1 y 99: "))
if numero >= 10:
    print("El número ingresado es de dos dígitos")
else:
    print("El número ingresado es de un dígito")

#-------------------------------------------------------

""" #13 Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima alguno de estos mensajes:
Si el promedio es >=7 mostrar "Promocionado".
Si el promedio es >=4 y <7 mostrar "Regular".
Si el promedio es <4 mostrar "Reprobado". """

nota1 = int(input("Ingrese la primera nota del alumno: "))
nota2 = int(input("Ingrese la segunda nota del alumno: "))
nota3 = int(input("Ingrese la tercera nota del alumno: "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 7:
    print("Promocionado")
elif promedio >= 4 :
    print("Regular")
else:
    print("Reprobado")

#------------------------------------------------------

""" #14 Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos."""

numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))
numero3 = int(input("Ingrese el tercer valor: "))
print("El numero mayor es: ")

if numero1 > numero2:
    if numero1 > numero3:
        print(numero1)
    else:
        print(numero3)
else:
    if numero2 > numero3:
        print(numero2)
    else:
        print(numero3)

#-------------------------------------------------------------

""" #15 Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero) """

numero = int(input("Ingrese un numero: "))
print("El numero ingresado es: ")
if numero == 0:
    print("nulo")
else:
    if numero > 0:
        print("Positivo")
    else:
        print("Negativo")

#-------------------------------------------------------------

""" #16 Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor. """

numero = int(input("Ingrese un numero positivo de hasta tres cifras: "))
print("El numero ingresado tiene ")
if numero <= 9:
    print("una cifra.")
else:
    if numero <= 99:
        print("dos cifras.")
    else:
        if numero <= 999:
            print("tres cifras.")
        else:
            print("más de tres cifras.")

#--------------------------------------------------------

""" #16 Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
	#Nivel máximo:	Porcentaje>=90%.
	#Nivel medio:	Porcentaje>=75% y <90%.
	#Nivel regular:	Porcentaje>=50% y <75%.
	#Fuera de nivel:	Porcentaje<50%.  """

preguntas_realizadas = int(input("Ingrese la cantidad de preguntas realizadas: "))
total_respuestas = int(input("Ingrese la cantidad de respuestas correctas: "))
porcentaje = (total_respuestas * 100) / preguntas_realizadas
if porcentaje >= 90:
    print("Nivel máximo")
else:
    if porcentaje >= 75:
        print("Nivel medio")
    else:
        if porcentaje >= 50:
            print("Nivel regular")
        else:
            print("Fuera de nivel")

#---------------------------------------------------------------

""" #18 Confeccionar un programa que lea por teclado tres números enteros distintos
#y nos muestre el mayor."""

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
print("El numero mayor es ")

if numero1 > numero2 and numero1 > numero3:
    print(numero1)
else:
    if numero2 > numero3:
        print(numero2)
    else:
        print(numero3)

#-----------------------------------------------------------------

""" #19 Se carga una fecha (día, mes y año) por teclado.
Mostrar un mensaje si corresponde al primer trimestre del año
(enero, febrero o marzo) Cargar por teclado el valor numérico del día, mes y
año. Ejemplo: dia:10 mes:2 año:2018 """

dia = int(input("Ingrese un día: "))
mes = int(input("Ingrese un mes: "))
anio = int(input("Ingrese un año: "))

if mes == 1 or mes == 2 or mes == 3:
    print("El mes corresponde al primer trimestre")
else:
    print("Fin")

#----------------------------------------------------------------------------

""" #20 Realizar un programa que pida cargar una fecha cualquiera,
luego verificar si dicha fecha corresponde a Navidad """

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

if dia == 25 and mes == 12:
    print("Es Navidad!")

#-------------------------------------------------------------------------


