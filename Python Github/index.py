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

""" #21 Se ingresan por teclado tres números, si todos los valores ingresados
#son menores a 10, imprimir en pantalla la leyenda
#"Todos los números son menores a diez """

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))

if num1 < 10 and num2 < 10 and num3 < 10:
    print("Todos los números son menores a diez")

#--------------------------------------------------------------------

""" #22 Se ingresan por teclado tres números, si al menos uno de los valores
ingresados es menor a 10, imprimir en pantalla la leyenda
#"Alguno de los números es menor a diez". """

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))

if num1 < 10 or num2 < 10 or num3 < 10:
    print("Alguno de los números es menor a diez")

#-----------------------------------------------------------------
""" #23 Se ingresan tres valores por teclado, si todos son iguales se imprime
la suma del primero con el segundo y a este resultado se lo multiplica
por el tercero"""

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))

if num1 == num2 and num1 == num3:
    resultado = (num1 + num2) * num3
    print(resultado)
 
#-----------------------------------------------------------------------------

""" #24 Escribir un programa que pida ingresar la coordenada de un punto en el plano,
es decir dos valores enteros x e y (distintos a cero).
Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto.
(1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)"""

x = int(input("Ingrese la coordenada X: "))
y = int(input("Ingrese la coordenada Y: "))

if x > 0 and y > 0:
    print("X e Y se encuentran en el cuadrante 1")
else:
    if x > 0 and y < 0:
        print("X e Y se encuentran en el cuadrante 4")
    else:
        if x < 0 and y > 0:
            print("X e Y se encuentran en el cuadrante 2")
        else:
            print("X e Y se encuentran en el cuadrante 3")
            
#----------------------------------------------------------------------------

""" #25 De un operario se conoce su sueldo y los años de antigüedad.
Se pide confeccionar un programa que lea los datos de entrada e informe:
a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior
a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años,
otorgarle un aumento de 5 %.
c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla
sin cambios. """

sueldo = int(input("Ingresar el sueldo del operario: "))
antiguedad = int(input("Ingresar la antiguedad del operario: "))

if sueldo < 500 and antiguedad >= 10:
    porcentaje = sueldo * 0.20
    sueldo += porcentaje
    print("El sueldo a pagar es ", sueldo)
else:
    if sueldo < 500 and antiguedad < 10:
        porcentaje = sueldo * 0.05
        sueldo += porcentaje
        print("El sueldo a pagar es ", sueldo)
    else:
        if sueldo >= 500:
            print("El sueldo a pagar es ", sueldo)

#-------------------------------------------------------------------

""" #26 Escribir un programa en el cual: dada una lista de tres valores numéricos
distintos se calcule e informe su rango de variación
(debe mostrar el mayor y el menor de ellos)"""

numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))
numero3 = int(input("Ingrese el tercer valor: "))

if numero1 < numero2 and numero1 < numero3:
    print("El numero menor es: ",numero1)
else:
    if numero2 < numero3:
        print("El numero menor es: ",numero2)
    else:
        print("El numero menor es: ",numero3)

if numero1 > numero2 and numero1 > numero3:
    print("El numero mayor es: ",numero1)
else:
    if numero2 > numero3:
        print("El numero mayor es: ",numero2)
    else:
        print("El numero mayor es: ",numero3)

#--------------------------------------------------------------------

""" #27 Realizar un programa que imprima en pantalla los números del 1 al 100."""

x = 1
while x <= 100:
    print(x)
    x+= 1

#---------------------------------------------------------------------

""" #28 Codificar un programa que solicite la carga de un valor positivo
y nos muestre desde 1 hasta el valor ingresado de uno en uno."""

x = 1
numero = int(input("Ingrese un numero positivo: "))

while x <= numero:
    print(x)
    x+=1

#-----------------------------------------------------------------------------

""" #29 Desarrollar un programa que permita la carga de 10 valores por teclado
y nos muestre posteriormente la suma de los valores ingresados y su promedio."""

x = 1
suma = 0
while x <=10:
    valor= int(input("Ingrese un valor: "))
    suma += valor
    x+=1

promedio = suma // 10
print("La suma de los valores es ",suma)
print("El promedio de los valores es ",promedio)

#-----------------------------------------------------------------------

"""#30 Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida ingresar por teclado la cantidad de piezas
a procesar y luego ingrese la longitud de cada perfil;
sabiendo que la pieza cuya longitud esté comprendida en el rango de
1.20 y 1.30 son aptas.
Imprimir por pantalla la cantidad de piezas aptas que hay en el lote."""


x = 1
cantidad = 0
n = int(input("Ingrese la cantidad de piezas: "))
while x <= n:
    longitud= float(input("Ingrese la longitud de cada perfil: "))
    if longitud >= 1.20 and longitud <= 1.30:
        cantidad +=1
    x+=1
print("Cantidad de piezas aptas: ",cantidad)

#----------------------------------------------------------------------------
"""#31 Escribir un programa que solicite ingresar 10 notas de alumnos y nos
informe cuántos tienen notas mayores o iguales a 7 y cuántos menores."""

x = 1
mas_7 = 0
menos_7 = 0
while x <= 10:
    nota = int(input("Ingrese las notas: "))
    if nota >= 7:
        mas_7 += 1
    else:
        menos_7 += 1
    x += 1
print("Alumnos con nota mayor o igual a siete: ")
print(mas_7)
print("Alumnos con nota menor a siete: ")
print(menos_7)

#--------------------------------------------------------------------------

"""#32 Se ingresan un conjunto de n alturas de personas por teclado.
Mostrar la altura promedio de las personas."""



x = 1
suma = 0
personas = int(input("Ingrese la cantidad de personas: ")) 
while x <= personas:
    n = float(input("Ingrese la altura de las personas: "))
    suma += n
    x +=1
promedio = suma / personas
print("La altura promedio es: ")
print(promedio)

#---------------------------------------------------------------------

"""#33 En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
realizar un programa que lea los sueldos que cobra cada empleado e informe
cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300.
Además el programa deberá informar el importe que gasta la empresa
en sueldos al personal."""

x = 1
suma=0
mayor_sueldo = 0
menor_sueldo = 0
empleados = int(input("Ingrese la cantidad de empleados: "))
while x <= empleados:
    sueldos = float(input("ingrese los sueldos de los empleados: "))
    suma += sueldos
    if sueldos >= 100 and sueldos <= 300:
       menor_sueldo += 1
    else:
        mayor_sueldo += 1
    x += 1
print(menor_sueldo," son los empleados que cobran entre 100 y 300")
print(mayor_sueldo, " son los empleados que cobran más de 300")
print("En concepto de sueldo, la empresa gasta: ", suma)

#---------------------------------------------------------------------

#34 Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc
#(No se ingresan valores por teclado)

serie = 11
x = 1
while x <= 25:
    print(serie)
    serie += 11
    x += 1

#---------------------------------------------------------------------------------

#35 Mostrar los múltiplos de 8 hasta el valor 500.
#Debe aparecer en pantalla 8 - 16 - 24, etc
x = 8
while x<=500:
    print(x)
    x+=8

#-----------------------------------------------------------------------

"""#36 Realizar un programa que permita cargar dos listas de 15 valores cada una.
Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor
(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un
algoritmo."""

x = 1
lista1 = 0
lista2 = 0
print("Datos lista 1")
while x <= 15:
    numeros = int(input("Ingrese los valores: "))
    lista1 += numeros
    x +=1
    
x = 1
print("Datos lista 2")
while x <= 15:
    numeros = int(input("Ingrese los valores: "))
    lista2 += numeros
    x +=1
    
if lista1 > lista2:
    print("La lista 1 es mayor")
else:
    if lista2 > lista1:
        print("La lista 2 es mayor")
    else:
        print("Las listas son iguales")

#------------------------------------------------------------------

""" #37 Desarrollar un programa que permita cargar n números enteros y luego nos
informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional
(este operador retorna el resto de la división de dos valores,
por ejemplo 11%2 retorna un 1):	if valor%2==0: """

x = 1
num_par = 0
num_impar = 0
cantidad = int(input("Ingrese la cantidad de valores: "))
while x <= cantidad:
    num = int(input("ingrese los numeros: "))
    if num % 2 == 0:
        num_par += 1
    else:
        num_impar += 1
    x += 1
print("La cantidad de numeros pares es: ", num_par)
print("La cantidad de numeros impares es: ", num_impar)
        
#--------------------------------------------------------------------
"""#38 Realizar un programa que imprima en pantalla los números del 0 al 100.
Este problema lo podemos resolver perfectamente con el ciclo while pero
en esta situación lo resolveremos empleando el for."""

for x in range(101):
    print(x)

##Realizar un programa que imprima en pantalla los números del 20 al 30.


for x in range(20, 31):
    print(x)


#Realizar un programa que imprima en pantalla los númerosimpares del 1 al 100.


for x in range(1, 101, 2):
    print(x)

#-----------------------------------------------------------

""" #39 Desarrollar un programa que permita la carga de 10 valores por teclado y
nos muestre posteriormente la suma de los valores ingresados y su promedio.
Este problema ya lo desarrollamos, lo resolveremos empleando
la estructura for para repetir la carga de los diez valores por teclado."""
suma = 0
for x in range(10):
    valor=int(input("Ingrese un valor: "))
    suma += valor
print("La suma de los valores es ", suma)
promedio = suma // 10
print("El promedio de los valores es ", promedio)

#--------------------------------------------------------------------

#40 Escribir un programa que solicite por teclado 10 notas de alumnos y
#nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

superior = 0
inferior = 0
for x in range(10):
    notas = int(input("Ingrese las notas de los alumnos: "))
    if notas >= 7:
        superior +=1
    else:
        inferior += 1
print("Los alumnos con nota mayor igual a 7 son: ", superior)
print("Los alumnos con nota inferior a 7 son: ", inferior)
    
#---------------------------------------------------------------------------------

""" #41 Escribir un programa que lea 10 números enteros y luego muestre
cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5.
Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez.
multiplos_3 = 0
multiplos_5 = 0"""

multiplos_3 = 0
multiplos_5 = 0
for x in range(10):
    valor = int(input("Ingrese diez valores: "))
    if valor % 3 == 0:
        multiplos_3+=1
    if valor % 5 == 0:
        multiplos_5+=1        
print("Numeros multiplos de 3: ", multiplos_3)
print("Numeros multiplos de 5: ", multiplos_5)

#-------------------------------------------------------------------------

#42 Codificar un programa que lea n números enteros y calcule la cantidad de
#valores mayores o iguales a 1000 (n se carga por teclado)

cantidad = 0
n = int(input("Ingrese la cantidad de valores: "))
for x in range(n):
    valor = int(input("Ingrese los valores: "))
    if valor >= 1000:
        cantidad += 1
print("Los numeros mayores o iguales a mil: ", cantidad)

#-------------------------------------------------------------------

#43 Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5
#al 50)


for i in range(11):
    tabla = i*5
    print(i," x 5 = ", tabla)


print("tabla del 7:")

for f in range(11):
    siete = f*7
    print(f, " x 7 = ", siete)

#------------------------------------------------------------------

""" #44 Confeccionar un programa que lea n pares de datos, cada par de datos
corresponde a la medida de la base y la altura de un triángulo.
El programa deberá informar:

a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12."""



n = int(input("Ingrese la cantidad de triangulos: "))
cantidad = 0
for x in range(n):
    base = int(input("Ingrese la medida de la base: "))
    altura = int(input("Ingrese la medida de la altura: "))
    superficie = (base * altura) / 2
    print("La base del triangulo es", base," la altura: ", altura, " y su superficie es ", superficie)
    if superficie > 12:
        cantidad += 1
print("Cantidad de triángulos con superficie mayor a 12: ", cantidad)

#------------------------------------------------------------------

#45 Desarrollar un programa que solicite la carga de 10 números e imprima
#la suma de los últimos 5 valores ingresados.

suma = 0
suma_ultimos= 0
for x in range(10):
    numeros = int(input("Ingrese los valores: "))
    suma+= numeros
    suma_ultimos = suma // 2
print("La suma de los ultimos cinco valores es igual a ", suma_ultimos)

## Opcion2

total = 0
for f in range(10):
    valor = int(input("Ingrese los numeros: "))
    if f >= 5:
        total+= valor
print("La suma de los ultimos cinco valores es igual a ", total)

#------------------------------------------------------------------------

""" #46 Confeccionar un programa que permita ingresar un valor del 1 al 10
y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)
Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9,
hasta el 36. """


valor = int(input("Ingrese un numero del 1 al 10: "))
for x in range(1, 13):
    tabla = x * valor
    print(x," x ", valor," = ", tabla)

#------------------------------------------------------------------------

"""#47 Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero
(tres lados iguales), isósceles (dos lados iguales), o escaleno
(ningún lado igual)
b) Cantidad de triángulos de cada tipo."""

cantidad_e = 0
cantidad_i = 0
cantidad_es = 0
triangulos = int(input("Ingrese la cantidad de triángulos: "))
for x in range(triangulos):
    lado1=int(input("Ingrese la medida del lado 1: "))
    lado2 =int(input("Ingrese la medida del lado 2: "))
    lado3 =int(input("Ingrese la medida del lado 3: "))
    if lado1 == lado2 and lado1 == lado3:
        cantidad_e += 1
        print("Triangulos equilateros")
    else:
        if lado1 == lado2 or lado1 == 3 or lado2 == lado3:
            cantidad_i += 1
            print("Triangulos isosceles")
        else:
            cantidad_es += 1
            print("Triangulos escalenos")
print("Cantidad de triángulos equiláteros: ", cantidad_e)
print("Cantidad de triángulos isosceles: ", cantidad_i)
print("Cantidad de triángulos escalenos: ", cantidad_es)

#-------------------------------------------------------------

"""#48 Escribir un programa que pida ingresar coordenadas (x,y) que representan
puntos en el plano. Informar cuántos puntos se han ingresado en el primer,
segundo, tercer y cuarto cuadrante.
Al comenzar el programa se pide que se ingrese la cantidad
de puntos a procesar."""

cuadrante1 = 0
cuadrante2 = 0
cuadrante3 = 0
cuadrante4 = 0
cantidad = int(input("Ingrese la cantidad de coordenadas X e Y: "))
for x in range(cantidad):
    coordenadas_x = int(input("Ingrese las coordenadas X: "))
    coordenadas_y = int(input("Ingrese las coordenadas Y: "))
    if coordenadas_x > 0 and coordenadas_y > 0:
        cuadrante1 += 1
    else:
        if coordenadas_x > 0 and coordenadas_y < 0:
            cuadrante4 += 1
        else:
            if coordenadas_x < 0 and coordenadas_y > 0:
                cuadrante2 += 1
            else:
                if coordenadas_x > 0 and coordenadas_y > 0:
                    cuadrante3 += 1
print("Cantidad de coordenadas X e Y en el cuadrante 1: ", cuadrante1)
print("Cantidad de coordenadas X e Y en el cuadrante 2: ", cuadrante2)
print("Cantidad de coordenadas X e Y en el cuadrante 3: ", cuadrante3)
print("Cantidad de coordenadas X e Y en el cuadrante 4: ", cuadrante4)

#----------------------------------------------------------------------

""" #49 Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares. """

negativos = 0
positivos = 0
multiplos = 0
pares = 0
for x in range(10):
    valor = int(input("Ingrese los valores: "))
    if valor < 0:
        negativos += 1
    else:
        positivos += 1
        
    if valor %15 == 0:
        multiplos += 1
    
    if valor % 2 == 0:
        pares += valor

print("Cantidad de numeros negativos: ", negativos)
print("Cantidad de numeros positivos: ", positivos)
print("Cantidad de múltiplos de 15: ", multiplos)
print("Valor acumulado de números pares : ", pares)

#--------------------------------------------------------------------

""" #50 Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos
tiene un promedio de edades mayor."""
edades_tm = 0
edades_tt = 0
edades_tn = 0
for x in range(5):
    edades = int(input("Ingrese las edades del turno mañana: "))
    edades_tm += edades
    promedio_tm = edades_tm // 5
for i in range(6):
    edades = int(input("Ingrese las edades del turno tarde: "))
    edades_tt += edades
    promedio_tt = edades_tt // 6
for i in range(11):
    edades = int(input("Ingrese las edades del turno noche: "))
    edades_tn += edades
    promedio_tn = edades_tn // 11
if promedio_tm > promedio_tt and promedio_tm > promedio_tn:
    print("Entre los tres turnos el promedio de edades mayor es el del turno mañana")
else:
    if promedio_tt > promedio_tm and promedio_tt > promedio_tn:
        print("Entre los tres turnos el promedio de edades mayor es el del turno tarde")
    else:
        if promedio_tn > promedio_tm and promedio_tn > promedio_tt:
            print("Entre los tres turnos el promedio de edades mayor es el del turno noche")
    
    
print("El promedio de edades del turno mañana es: ", promedio_tm)
print("El promedio de edades del turno tarde es: ", promedio_tt)
print("El promedio de edades del turno noche es: ", promedio_tn)

#-------------------------------------------------------------------------
""" #51 Mostrar la tabla de multiplicar del 5 empleando primero el while
y seguidamente de nuevo empleando el for."""


x = 5
while x <= 50:
    print(x)
    x+= 5


print("Tabla del 5 con estructura for:")
for x in range(11):
    tabla = x * 5
    print("5 x ",x," = ", tabla)

#---------------------------------------------------------------------

    """ #52 Realizar un programa que solicite la carga de valores enteros por teclado y
los sume. Finalizar la carga al ingresar el valor -1. Dejar como comentario
dentro del código fuente el enunciado del problema."""


suma = 0
cantidad = int(input("¿Cuantos numeros desea sumar? "))
for x in range(cantidad):
    numero = int(input("Ingrese los numeros: "))
    suma += numero
    if numero == -1:
        break #detiene el programa
print("La suma de los numeros es igual a ", suma)

#solucion del profesor:

suma_ = 0
valor = int(input("Ingrese un valor (-1 finaliza la carga): "))#carga primer valor
while valor != -1:
    suma_+= valor
    valor = int(input("Ingrese un valor (-1 finaliza la carga): "))#carga desde el valor 2 hasta el ultimo
print("La suma de los valores ingresados")
print(suma_)

#--------------------------------------------------------------------------

""" #53 Confeccionar un programa que solicite la carga de 10 valores reales
por teclado. Mostrar al final su suma. Definir varias líneas de comentarios
indicando el nombre del programa, el programador y la fecha de la última
modificación. Utilizar el caracter # para los comentarios."""

suma = 0
for x in range(10):
    valor = float(input("Ingrese un valor: "))
    suma+= valor
print("La suma de los valores es", suma)

#25-08-2022

#-----------------------------------------------------------------------------

""" #54 Realizar la carga por teclado del nombre, edad y altura de dos personas.
Mostrar por pantalla el nombre de la persona con mayor altura."""

print("Datos de la primera persona")
nombre_p1 = input("Ingrese el nombre: ")
edad_p1 = int(input("Ingrese la edad: "))
altura_p1 = float(input("Ingrese la altura:"))
print("Datos de la segunda persona")
nombre_p2 = input("Ingrese el nombre: ")
edad_p2 = int(input("Ingrese la edad: "))
altura_p2 = float(input("Ingrese la altura: "))
if altura_p1 > altura_p2:
    print("La persona más alta es ", nombre_p1)
else:
    print("La persona más alta es ", nombre_p2)

#---------------------------------------------------------------------------

""" #55 Realizar la carga de dos nombres por teclado. Mostrar cual de los dos
es mayor alfabéticamente o si son iguales.
(Se refiere al orden alfabetico, no a la cantidad de letras del nombre)"""

nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")
if nombre1 == nombre2:
    print("Ambos nombres son iguales alfabéticamente")
else:
    if nombre1 > nombre2:
        print(nombre1," es mayor alfabéticamente")
    else:
        print(nombre2," es mayor alfabéticamente")
    

#En la tabla de caracteres, las minusculas son mayores que las mayúsculas. Por
#ello, ana sería mayor que Ana

#-----------------------------------------------------------------------

""" #56 Realizar la carga de enteros por teclado. Preguntar después que ingresa
el valor si desea cargar otro valor debiendo el operador ingresar la cadena
'si' o 'no' por teclado. Mostrar la suma de los valores ingresados."""

valor1 =int(input("Ingrese un valor: "))
valor2 =int(input("Ingrese un valor: "))
respuesta = input("¿Desea ingresar un nuevo valor?(Responda si o no) ")

if respuesta == "si":
    nuevo_valor = int(input("Ingrese un nuevo valor: "))
    suma = valor1 + valor2 + nuevo_valor
    print("La suma de los tres valores es", suma)
else:
    if respuesta == "no":
        suma = valor1 + valor2
        print("La suma de los valores es",suma)

print(" ")
print("Solucion del profesor")
opcion = "si"
sumatoria = 0
while opcion == "si":
    valor = int(input("Ingrese un valor: "))
    sumatoria+= valor
    opcion = input("¿Desea cargar otro valor? (si/no)")
print("La suma de los valores es", sumatoria)

#Las mayusculas no tienen el mismo valor alfabético que las minusculas

#-------------------------------------------------------------------------------

""" #57 Realizar la carga de dos nombres de personas distintos.
Mostrar por pantalla luego ordenados en forma alfabética."""

nombre1= input("Ingrese el primer nombre: ")
nombre2= input("Ingrese el segundo nombre: ")
if nombre1<nombre2:
    print(nombre1, nombre2)
else:
    print(nombre2, nombre1)

#---------------------------------------------------------------------

""" #58 Realizar la carga del nombre de una persona y luego mostrar el primer
caracter del nombre y la cantidad de letras que lo componen"""

nombre = input("Ingrese un nombre: ")
print("Primera letra del nombre:", nombre[0])
print("Cantidad de letras del nombre ingresado: ", len(nombre))

#-----------------------------------------------------------------

""" #59 Solicitar la carga del nombre de una persona en minúsculas.
Mostrar un mensaje si comienza con vocal dicho nombre."""


nombre = input("Ingrese un nombre en minúsculas: ")

if nombre[0]== "a" or nombre[0]== "e" or nombre[0]== "i" or nombre[0]== "o" or nombre[0]== "u":
    print("El nombre ", nombre, " comienza con vocal")
else:
    print("El nombre ", nombre, " no lleva vocal")

#----------------------------------------------------------------------

""" #60 Ingresar un mail por teclado. Verificar si el string ingresado
contiene solo un caracter "@" """

mail = input("Ingrese su e-mail: ")
x = 0
cantidad = 0

while x < len(mail):
    if mail[x] == "@":
        cantidad += 1
    x+=1
if cantidad == 1:
    print("El mail ingresado contiene un @")
else:
    print("El mail ingresado es incorrecto.")
    
#----------------------------------------------------------------------

""" #61 Inicializar un string con la cadena "mAriA" luego llamar a sus métodos
upper(), lower() y capitalize(), guardar los datos retornados en otros string
y mostrarlos por pantalla."""

nombre = "mAríA"
print(nombre)
nombre1 = nombre.upper()
print(nombre1)
nombre2 = nombre.lower()
print(nombre2)
nombre3 = nombre.capitalize()
print(nombre3)

#---------------------------------------------------------------------------------

""" #62 Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco
se ingresaron. Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es "" """


oracion= input("Ingrese una oración: ")
x = 0
cantidad = 0
while x < len(oracion):
    if oracion[x] == " " :
        cantidad+=1
    x+=1
print("Dentro de la oracion, hay ", cantidad, " espacios vacíos.")

#-------------------------------------------------------------------------

""" #63 Ingresar una oración que pueden tener letras tanto en mayúsculas como
minúsculas. Contar la cantidad de vocales. Crear un segundo string con toda la
oración en minúsculas para que sea más fácil disponer la condición que verifica
que es una vocal. """

oracion = input("Ingrese una oración: ")
oracion1 = oracion.lower()
vocales = 0
x = 0

while x<len(oracion1):
    if oracion1[x] == "a" or oracion1[x] == "e" or oracion1[x] == "i" or oracion1[x] == "o" or oracion1[x] == "u":
        vocales+=1
    x+=1
print("La oración ingresada contiene, ",vocales," vocales")

#-----------------------------------------------------
""" #64 Solicitar el ingreso de una clave por teclado y almacenarla en una
cadena de caracteres. Controlar que el string ingresado tenga entre 10 y 20
caracteres para que sea válido, en caso contrario mostrar un mensaje de error."""

clave = input("Ingrese una clave: ")
if len(clave) >= 10 and len(clave) <= 20:
    print("La clave es válida")
else:
    print("La clave ingresada no es válida")

#-----------------------------------------------------------------------

""" #65 Definir una lista que almacene 5 enteros. Sumar todos sus elementos
y mostrar dicha suma."""

lista = [1,2,3,4,5]
suma = 0
x = 0

while x < len(lista):
    suma +=lista[x]
    x+=1
print("La lista almacenada", lista)
print("La suma de los valores es igual a ",suma)

#---------------------------------------------------------------------------

""" #66 Definir una lista por asignación que almacene los nombres de los
primeros cuatro meses de año. Mostrar el primer y último elemento de la
lista solamente."""

meses =["enero", "febrero", "marzo", "abril"]
print("Primer mes: ",meses[0])
print("Cuarto mes: ",meses[3])

#-------------------------------------------------------------------------

""" #67 Definir una lista por asignación que almacene en la primer
componente el nombre de un alumno y en las dos siguientes sus notas.
Imprimir luego el nombre y el promedio de las dos notas. """

alumno = ["Olivera", 9, 10]
promedio = (alumno[1] + alumno[2]) // 2
print("El alumno ", alumno[0], " tiene el promedio: ", promedio)

#----------------------------------------------------------------------

""" #68 Definir por asignación una lista con 8 elementos enteros.
Contar cuantos de dichos valores almacenan un valor superior a 100 """

lista =[254, 77, 8, 122, 109, 5, 4, 11]
x=0
mayores = 0
while x <len(lista):
    if lista[x] > 100:
        mayores+=1
    x+=1
print("Lista almacenada: ", lista)
print("Hay ", mayores, " números mayores a 100")

#-------------------------------------------------------------------------

""" #69 Definir una lista por asignación con 5 enteros. Mostrar por pantalla
solo los elementos con valor iguales o superiores a 7."""

lista = [45, 1, 7, 2, 8]
siete = 0
for x in range(len(lista)):
    if lista[x]>=7:
        print("Numeros mayores/iguales a 7: ",lista[x])
print("Lista almacenada: ",lista)

#------------------------------------------------------------------

""" #70 Definir una lista que almacene por asignación los nombres de 5
personas. Contar cuantos de esos nombres tienen 5 o más caracteres."""

lista = ["juan", "pedro", "luis", "maria", "joaquin"]
x = 0
nombres = 0
while x < len(lista):
    if len(lista[x]) >= 5:
        nombres+=1
    x+=1
print("Hay ",nombres," nombres con 5 o más caracteres en la lista almacenada: ")
print(lista)
              
#-------------------------------------------------------------------------------

""" #71 Definir una lista vacía y luego solicitar la carga de 5 enteros
por teclado y añadirlos a la lista. Imprimir la lista generada."""

lista = []
x=0
while x < 5:
    enteros = int(input("Ingrese un numero : "))
    lista.append(enteros)
    x+=1
print("Lista: ",lista)


#--------------------------

lista1 = []
for x in range(5):
    valores = int(input("Ingrese un valor: "))
    lista1.append(valores)
print("Lista", lista1)

#-----------------------------------------------------------------

""" #72 Realizar la carga de valores enteros por teclado, almacenarlos en una
lista. Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente
el tamaño de la lista."""

lista = [ ]
valores = int(input("ingrese un numero (0 finaliza la carga): "))
while valores != 0:
    lista.append(valores)
    valores = int(input("ingrese un numero: "))
print("Lista almacenada:", lista)
print("Largo de la lista: ",len(lista))

#---------------------------------------------------------------

""" #73 Almacenar en una lista los sueldos (valores float) de 5 operarios.
Imprimir la lista y el promedio de sueldos."""
suma = 0
promedio = 0
x = 0
s_operarios = []
while x < 5:
    sueldos = float(input("Ingrese los sueldos: "))
    s_operarios.append(sueldos)
    suma += s_operarios[x]
    promedio = suma / len(s_operarios)
    x +=1
print("Lista de sueldos: ", s_operarios)
print("Promedio de sueldos: ", promedio)

#------------------------------------------------------------------

""" #74 Cargar por teclado y almacenar en una lista las alturas de 5 personas
(valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas
que el promedio y cuántas más bajas."""

lista = []
x=0
suma = 0
y=0
mas = 0
menos = 0
while x < 5:
    alturas = float(input("Ingrese la altura: "))
    lista.append(alturas)
    suma += alturas
    x+=1
print("lista: ",lista)
promedio = suma / len(lista)
print("Promedio de alturas:", promedio)
while y < len(lista):
    if lista[y] < promedio:
        menos +=1
    else:
        mas +=1
    y+=1
    
print("Cantidad de personas mayores al promedio: ", mas)
print("Cantidad de personas menores al promedio: ", menos)

#-----------------------------------------------------------------

""" #75 Una empresa tiene dos turnos (mañana y tarde) en los que trabajan
8 empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa que
permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos."""

mañana = []
tarde = []
empleados = []
for x in range(8):
    sueldos = float(input("Ingrese los sueldos: "))
    empleados.append(sueldos)
mañana = empleados[0:4]
tarde = empleados[4:9]
print("sueldos empleados turno mañana: ", mañana)
print("sueldos empleados turno tarde: ", tarde)

#---------------------------------------------------------------------

""" #76 Crear y cargar una lista con 5 enteros. Implementar un algoritmo
que identifique el mayor valor de la lista """

lista = []
for x in range(5):
    enteros = int(input("Ingrese un número: "))
    lista.append(enteros)

#algoritmo para sacar el > elemento de la lista:

mayor = lista[0]
for x in range(1,5):
    if lista[x] > mayor:
        mayor = lista[x]
print("Lista: ", lista)
print("Numero mayor: ", mayor)

#-------------------------------------------------------------------------

""" #77 Crear y cargar una lista con 5 enteros por teclado.Implementar un
algoritmo que identifique el menor valor de la lista y la posición
donde se encuentra. """
lista = []
for x in range (5):
    enteros = int(input("Ingrese un valor: "))
    lista.append(enteros)
posicion = 0
menor = lista [0]
for x in range(1, 5):
    if lista[x] < menor:
        menor = lista[x]
        posicion = x

print("Lista: ", lista)
print("Número menor: ", menor)
print("Posicion del número: ", posicion)

#----------------------------------------------------------------------

""" #78 Ingresar por teclado los nombres de 5 personas y almacenarlos en
una lista. Mostrar el nombre de persona menor en orden alfabético"""

lista = []
for x in range(5):
    nombres = input("Ingrese los nombres: ")
    lista.append(nombres)

primera = lista[0]
for x in range(1,5):
    if lista[x]<primera:
        primera = lista[x]
print("Lista de nombres: ", lista)
print("Primer nombre en orden: ", primera)
        
#----------------------------------------------------------------------------

""" #79 Cargar una lista con 5 elementos enteros.
Imprimir el mayor y un mensaje si se repite dentro de la lista
(es decir si dicho valor se encuentra en 2 o más posiciones en la lista)"""

lista = []
for x in range(5):
    enteros = int(input("Ingrese un número: "))
    lista.append(enteros)

#número mayor
mayor = lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor= lista[x]
print("Lista: ", lista)
print("Número mayor: ", mayor)


# para ver si el numero se repite:
repeticion = 0
for x in range(5):
    if lista[x]== mayor:
        repeticion += 1
if repeticion > 1:
    print("El valor mayor se encuentra repetido ", repeticion, " veces en la lista")

#-----------------------------------------------------------------------------------

""" #80 Desarrollar un programa que permita cargar 5 nombres de personas
y sus edades respectivas. Luego de realizar la carga por teclado de todos
los datos imprimir los nombres de las personas mayores de edad (mayores o
iguales a 18 años)"""

nombres = []
edades = []
for i in range(5):
    l_nombres = input("Ingrese un nombre: ")
    nombres.append(l_nombres)
    l_edades = int(input("Ingrese la edad: "))
    edades.append(l_edades)
for x in range(5):
    if edades[x] >=18:
        print("Las personas mayores son: ", nombres[x])

#------------------------------------------------------------------------

""" #81 Crear y cargar dos listas con los nombres de 5 productos en una
y sus respectivos precios en otra. Definir dos listas paralelas. Mostrar
cuantos productos tienen un precio mayor al primer producto ingresado."""

productos = []
precios = []
for x in range(5):
    producto = input("Ingrese el producto: ")
    productos.append(producto)
    precio = float(input("Ingrese el precio del producto: "))
    precios.append(precio)

cantidad = 0
for x in range(1, 5):
    if precios[0]<precios[x]:
        cantidad+=1
if cantidad > 1:
    print("Cantidad de productos cuyo precio es mayor al primero: ", cantidad)

#----------------------------------------------------------------------------------

""" #82 En un curso de 4 alumnos se registraron las notas de sus exámenes
y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas
paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno.
En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno"
si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior
a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”."""

nombres = []
notas = []
for x in range(4):
    nombre = input("Ingrese el nombre: ")
    nombres.append(nombre)
    nota = int(input("Ingrese la nota: "))
    notas.append(nota)
cantidad = 0
for x in range(4):
    print(nombres[x])
    print(notas[x])
    if notas[x] >= 8:
        print("Muy Bueno")
        cantidad +=1
    else:
        if notas[x]>= 4:
            print("Bueno")
        else:
            print("Insuficiente")
print("Cantidad de alumnos con condicion Muy bueno: ", cantidad)
        
#----------------------------------------------------------------------

""" #83 Realizar un programa que pida la carga de dos listas numéricas
enteras de 4 elementos cada una. Generar una tercer lista que surja de
la suma de los elementos de la misma posición de cada lista. Mostrar esta
tercer lista."""

lista1 = []
lista2 = []
lista3 = []
for x in range(4):
    numero1 = int(input("Ingrese una número: "))
    lista1.append(numero1)
    numero2 = int(input("Ingrese una número: "))
    lista2.append(numero2)
for x in range(4):
    suma = lista1[x]+lista2[x]
    lista3.append(suma)
print("Lista 1: ", lista1)
print("Lista 2: ", lista2)
print("Lista 3: ", lista3)

#------------------------------------------------------------

# Ordenamiento de elementos de una lista - Ordenamiento burbuja

""" #84 Se debe crear y cargar una lista donde almacenar 5 sueldos.
Desplazar el valor mayor de la lista a la última posición."""
sueldos = []
for x in range(5):
    sueldo = float(input("Ingrese el sueldo: "))
    sueldos.append(sueldo)
print("Lista de sueldos", sueldos)


for x in range(4):
    if sueldos[x] > sueldos[x+1]:
        aux = sueldos[x]
        sueldos[x] = sueldos[x+1]
        sueldos[x+1] = aux
print("Lista de sueldos: ", sueldos)

#------------------------------------------------------------------------
""" #85 Se debe crear y cargar una lista donde almacenar 5 sueldos.
Ordenar de menor a mayor la lista. """

sueldos = []
for x in range(5):
    sueldo = int(input("Ingrese un sueldo: "))
    sueldos.append(sueldo)
print("Lista original: ", sueldos)

for k in range(4):
    for x in range (4-k):
        if sueldos[x] > sueldos[x+1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x+1]
            sueldos[x+1] = aux
print("Lista ordenada", sueldos)

#----------------------------------------------------------

""" #86 Crear una lista y almacenar los nombres de 5 países. Ordenar
alfabéticamente la lista e imprimirla. """

paises = []
for x in range(5):
    pais = input("Ingrese un país: ")
    paises.append(pais)
print("Lista original de países: ", paises)

for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux
print("Lista de países ordenada alfabéticamente: ", paises)

#------------------------------------------------------------------------

""" #87 Solicitar por teclado la cantidad de empleados que tiene la empresa.
Crear y cargar una lista con todos los sueldos de dichos empleados.
Imprimir la lista de sueldos ordenamos de menor a mayor. """
sueldos = []
empleados = int(input("¿Cuantos empleados tiene la empresa? "))
for x in range(empleados):
    sueldo = int(input("Ingrese el sueldo de cada empleado: "))
    sueldos.append(sueldo)
print("Lista de sueldos", sueldos)

for k in range(empleados-1):
    for x in range(empleados-1-k):
        if sueldos[x] > sueldos[x+1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x+1]
            sueldos[x+1]=aux
print("Lista ordenada: ", sueldos)

#-----------------------------------------------------------------------

""" #88 Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor
y mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente."""

lista = []
for x in range(5):
    valores = int(input("Ingrese un valor: "))
    lista.append(valores)
print("Lista: ", lista)

#Orden de menor a mayor
for k in range(4):
    for x in range(4-k):
        if lista[x]>lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux
print("Lista ordenada de menor a mayor", lista)

#Orden de mayor a menor

for k in range(4):
    for x in range(4-k):
        if lista[x]<lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux
print("Lista ordenada de mayor a menor: ", lista)

#-----------------------------------------------------------------

""" #89 Confeccionar un programa que permita cargar los nombres de 5 alumnos
y sus notas respectivas. Luego ordenar las notas de mayor a menor. Imprimir
las notas y los nombres de los alumnos."""

alumnos = []
notas = []
for x in range(5):
    nombres= input("Ingrese nombre del alumno: ")
    alumnos.append(nombres)
    nota = int(input("Ingrese la nota del alumno: "))
    notas.append(nota)
print("Original", alumnos, notas)

#orden notas mayor a menor

for k in range(4):
    for x in range(4-k):
        if notas[x]<notas[x+1]:
            aux=notas[x]
            notas[x]=notas[x+1]
            notas[x+1]=aux
            aux1 = alumnos[x]
            alumnos[x]=alumnos[x+1]
            alumnos[x+1]=aux1

print("Calificaciones: ")
for x in range(5):
    print(alumnos[x],notas[x])

#------------------------------------------------------------------

""" #90 Crear y cargar en un lista los nombres de 5 países y en otra lista
paralela la cantidad de habitantes del mismo. Ordenar alfabéticamente e
imprimir los resultados. Por último ordenar con respecto a la cantidad
de habitantes (de mayor a menor) e imprimir nuevamente."""

paises = []
habitantes = []
for x in range(5):
    pais = input("Ingrese un pais: ")
    paises.append(pais)
    cantidad = int(input("Ingrese la cantidad de habitantes: "))
    habitantes.append(cantidad)
print(paises, habitantes)

#Orden alfabético de los paises:
for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux1 = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux1
            aux2=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1] = aux2
print("Paises ordenados alfabéticamente: ")
for x in range(5):
    print(paises[x], habitantes[x])

#Ordenamiento numérico:
for k in range(4):
    for x in range(4-k):
        if habitantes[x]<habitantes[x+1]:
            aux=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1
print("Lista de habitantes ordenada de mayor a menor")
for x in range(5):
    print(habitantes[x],paises[x])

#---------------------------------------------------------------------
