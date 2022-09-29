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

""" #91 Crear una lista por asignación. La lista tiene que tener cuatro
elementos. Cada elemento debe ser una lista de 3 enteros.
Imprimir sus elementos accediendo de diferentes modos."""

lista = [[1,2,3,],[4,5,6],[7,8,9,],[10,11,12]]
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])

#---------------------------------------------------------------------

""" #92 Crear una lista por asignación. La lista tiene que tener 2 elementos.
Cada elemento debe ser una lista de 5 enteros.
Calcular y mostrar la suma de cada lista contenida en la lista principal."""
lista = [[1,2,3,4,5],[6,7,8,9,10]]

# metodo 1:
suma1=lista[0][0]+lista[0][1]+lista[0][2]+lista[0][3]+lista[0][4]
print(suma1)
suma2=lista[1][0]+lista[1][1]+lista[1][2]+lista[1][3]+lista[1][4]
print(suma2)

#metodo 2: 
suma = 0
suma1= 0
for x in range(len(lista[0])):
    suma += lista[0][x]
for x in range(len(lista[1])):
    suma1 += lista[1][x]
print(suma)
print(suma1)

#metodo 3 for anidado:

for k in range(len(lista)):
    suma = 0
    for x in range(len(lista[k])):
        suma+=lista[k][x]
    print("Suma: ", suma)

#----------------------------------------------------------------------------

""" #93 Crear una lista por asignación. La lista tiene que tener 5 elementos.
Cada elemento debe ser una lista, la primera lista tiene que tener un elemento,
la segunda dos elementos, la tercera tres elementos y así sucesivamente.
Sumar todos los valores de las listas."""

lista = [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]
suma = 0
for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma+=lista[k][x]
print("Lista: ", lista)
print("Suma:", suma)

#----------------------------------------------------------------------------

""" #94 Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores
a 50 del primer elemento de "lista".
Volver a imprimir la lista. """

lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
print("Lista: ", lista)

for x in range(len(lista)):
    if lista[0][x]>50:
        lista[0][x] = 0
print("Lista modificada: ", lista)

#--------------------------------------------------------------------------------

""" #95 Se tiene la siguiente lista:
lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores
a 10 contenidos en todos los elementos de la variable "lista".
Volver a imprimir la lista."""

lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
print("Lista: ", lista)
for k in range(len(lista)):
    for x in range(len(lista[k])):
        if lista[k][x] > 10:
            lista[k][x] = 0
print("Lista modificada: ", lista)

#-------------------------------------------------------------------------------
""" #96 crear una lista por asignación con la cantidad de elementos de tipo
lista que usted desee. Luego imprimir el último elemento de la lista principal"""

lista = [["hola", "chau"], [14,15], [True, False]]
print("Lista: ", lista)
print("Ultimo elemento: ", lista[2])
print()
#Solucion del profesor: "
print(lista[len(lista)-1])

#-------------------------------------------------------------------------------
""" #97 Crear y cargar una lista con los nombres de tres alumnos. Cada alumno
tiene dos notas, almacenar las notas en una lista paralela. Cada componente
de la lista paralela debe ser también una lista con las dos notas.
Imprimir luego cada nombre y sus dos notas."""

alumnos = []
notas = []
for x in range(3):
    alumno = input("Ingrese el nombre del alumno: ")
    alumnos.append(alumno)
    nota1 = int(input("Ingrese la primera nota: "))
    nota2 = int(input("Ingrese la segunda nota: "))
    notas.append([nota1, nota2])

for x in range(3):
    print(alumnos[x], notas[x][0], notas[x][1])

#-------------------------------------------------------------------------------
""" #98 Se tiene que cargar la siguiente información:
· Nombres de 3 empleados
· Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.

Confeccionar el programa para:

a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses.
d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado. """

#a:
empleados = []
sueldos = []
totalingresos=[]
for x in range(3):
    empleado = input("Ingrese el nombre del empleado: ")
    empleados.append(empleado)
    sueldo1 = int(input("Ingrese el sueldo del empleado: "))
    sueldo2 = int(input("Ingrese el sueldo del empleado: "))
    sueldo3 = int(input("Ingrese el sueldo del empleado: "))
    sueldos.append([sueldo1, sueldo2, sueldo3])
#b:  
suma = 0
for x in range(3):
    suma = sueldos[x][0] + sueldos[x][1] + sueldos[x][2]
    totalingresos.append(suma)
#c:
for x in range(3):
    print("Total ingresos de empleado: ", empleados[x], totalingresos[x])

#d:
posmayor = 0
mayor = totalingresos[0]
for x in range(3):
    if totalingresos[x]>mayor:
        mayor = totalingresos[x]
        posmayor= x
print("Empleado con mayor ingresos es ", empleados[posmayor], "cuyo ingreso es: ", mayor)


#----------------------------------------------------------------------------------

""" #99 Solicitar por teclado dos enteros. El primer valor indica la cantidad
de elementos que crearemos en la lista. El segundo valor indica la cantidad
de elementos que tendrá cada una de las listas internas a la lista principal.

Mostrar la lista y la suma de todos sus elementos."""

lista = []
elementos = int(input("¿Cuantos elementos tendrá la lista? "))
elsub = int(input("¿Cuántos elementos tendrán las sublistas? "))
for k in range(elementos):
    lista.append([])
    for x in range(elsub):
        valor= int(input("Ingrese un valor: "))
        lista[k].append(valor)

print("Lista original: ", lista)

suma=0
for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma+=lista[k][x]
print("Suma de los elementos: ", suma)

#--------------------------------------------------------------------------------
""" #100 Definir dos listas de 3 elementos.
La primera lista es una sublista con el nombre del padre y la madre de una familia.
La segunda lista está constituida por listas con los nombres de los hijos
de cada familia. Puede haber familias sin hijos.

Imprimir los nombres del padre, la madre y sus respectivos hijos.

También imprimir solo el nombre del padre y la cantidad de hijos que tiene. """

padres = []
hijos = []
for k in range(3):
    padre=input("Ingrese el nombre del padre: ")
    madre = input("Ingrese el nombre de la madre: ")
    padres.append([padre, madre])
    cantidad= int(input("¿Cuantos hijos tiene la familia? "))
    hijos.append([])
    for x in range(cantidad):
        hijo= input("Ingrese el nombre del hijo: ")
        hijos[k].append(hijo)
        
print("Padre, madre y sus hijos: ")
for k in range(3):
    print("Padre: ",padres[k][0], "Madre: ",padres[k][1])
    for x in range(len(hijos[k])):
        print("Hijos: ",hijos[k][x])

print("Lista de padres e hijos: ")
for x in range(3):
    print("Padre: ",padres[x][0], " Cantidad de hijos: ",len(hijos[x]))

#---------------------------------------------------------------------------
""" #101 Se desea saber la temperatura media trimestral de cuatro paises. Para
ello se tiene como dato las temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del país y seguidamente las tres temperaturas
medias mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.

a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
c - Calcular la temperatura media trimestral de cada país.
d - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
e - Imprimir el nombre del pais con la temperatura media trimestral mayor. """

#a
paises = []
temperaturas = []
for x in range(4):
    nombre = input("Ingrese el nombre del pais: ")
    paises.append(nombre)
    t1 = int(input("Ingrese la temperatura media: "))
    t2 = int(input("Ingrese la temperatura media: "))
    t3 = int(input("Ingrese la temperatura media: "))
    temperaturas.append([t1, t2, t3])
#b así no sale impreso entre []
print("Paises y temperaturas medias")
for x in range(4):
    print(paises[x], temperaturas[x][0], temperaturas[x][1], temperaturas[x][2])

#c
suma = 0
promedio = 0
ttrim = []
for x in range(4):
    suma = temperaturas[x][0] + temperaturas[x][1] + temperaturas[x][2]
    promedio = suma / 3
    ttrim.append(promedio)

#d
for x in range(4):
    print(paises[x], "temperatura medias trimestral: ", ttrim[x])

#e
tmayor = ttrim[0]
posicion = 0
for x in range(1, 4):
    if ttrim[x]>tmayor:
        tmayor=ttrim[x]
        posicion = x
print("País con la temperatura media trimestral mayor:", paises[posicion], " con una temperatura de ", tmayor)

#---------------------------------------------------------------------------------
""" #102 Definir una lista y almacenar los nombres de 3 empleados. Por otro
lado definir otra lista y almacenar en cada elemento una sublista con los
números de días del mes que el empleado faltó.

1. Imprimir los nombres de empleados y los días que faltó.
2. Mostrar los empleados con la cantidad de inasistencias.
3. Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días."""

empleados = []
faltas = []
for k in range(3):
    nombre = input("Ingrese nombre del empleado: ")
    empleados.append(nombre)
    veces = int(input("¿Cuantas veces falto el empleado? "))
    faltas.append([])
    for x in range(veces):
        dia = int(input("Ingrese el número de día que faltó: "))
        faltas[k].append(dia)

for x in range(3):
    print("Empleado: ", empleados[x], "Dias del mes en que faltó: ", faltas[x])

#2
totalfaltas=[]
for x in range(3):
    totalfaltas.append(len(faltas[x]))
    print("Cantidad de inasistencias de los empleados:", empleados[x],totalfaltas[x])


#3. mostrar el nombre o los nombres de empleados que faltaron menos días.
posmenor = 0
menor = totalfaltas[0]
for x in range(1,3):
    if totalfaltas[x]<menor:
        menor = totalfaltas[x]
        posmenor=x
print("Empleado con menor cantidad de faltas:")
print(empleados[posmenor], " cantidad de faltas: ", menor)

#-------------------------------------------------------------------------------
#EJERCICIO 102 - SOLUCION DEL PROFESOR

"""Definir una lista y almacenar los nombres de 3 empleados; en otra almacenar
en sublistas los números de días del mes que el empleado faltó.
a. Imprimir los nombres de empleados y los días que faltó.
b Mostrar los empleados con la cantidad de inasistencias.
c. Mostrar el nombre o los nombres de empleados que faltaron menos días."""

empleados = []
faltas = []
for k in range(3):
    nombre = input("Ingrese el nombre del empleado: ")
    empleados.append(nombre)
    cantidad = int(input("¿cuantos días faltó el empleado? "))
    faltas.append([]    )
    for x in range(cantidad):
        dia = int(input("Ingrese el dia en el que el empleado falto "))
        faltas[k].append(dia)

print("Nombre de empleados y dias que faltó")
for k in range(3):
    print(empleados[k])
    for x in range(len(faltas[k])):
        print(faltas[k][x])

print("Nombre empleado y cantidad de inasistencias")
for x in range(3):
    print(empleados[x], len(faltas[x]))

menor = len(faltas[0])
for x in range(1,3):
    if len(faltas[x])< menor:
        menor = len(faltas[x])

print("Empleado/s con menor cantidad de inasistencias")
for x in range(3):
    if len(faltas[x]) == menor:
        print(empleados[x])

#-----------------------------------------------------------------------------

""" #104 Desarrollar un programa que cree una lista de 50 elementos. El primer
elemento es una lista con un elemento entero, el segundo elemento es una lista
de dos elementos etc.
La lista debería tener esta estructura y asignarle esos valores a medida
que se crean los elementos:
[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], etc....]"""
#opcion 1

lista=[]
contador = 1
for k in range(50):
    lista.append([])
    numero = 1
    for x in range(contador):
        lista[k].append(numero)
        numero+=1
    contador+=1
print(lista)

#opcion2
lista1=[]
for k in range(50):
    lista1.append([])
    for x in range(len(lista1)):
        lista1[k].append(x+1)
print(lista1)

#-------------------------------------------------------------------

""" #105 Crear una lista por asignación con 5 enteros. Eliminar el primero,
el tercero y el último de la lista."""

lista = [77, 25, 2, 5, 7]
print(lista)
lista.pop(0)
lista.pop(1)
lista.pop(2)
print(lista)

#-----------------------------------------------------------------------------
""" #106 Crear una lista y almacenar 10 enteros pedidos por teclado.
Eliminar todos los elementos que sean iguales al número entero 5."""

lista = []
for x in range(10):
    numeros = int(input("Ingrese un numero: "))
    lista.append(numeros)
print(lista)

#opcion 1
posicion = 0
while posicion<len(lista):
    if lista[posicion] == 5:
        lista.pop(posicion)
    else:
        posicion = posicion+1
print(lista)

#opcion 2

posicion1 = 0
while posicion1<len(lista):
    if lista[posicion1] == 5:
        del(lista[posicion1])
    else:
        posicion1 = posicion1+1
print(lista)

#---------------------------------------------------------------------------

""" #107 Crear dos listas paralelas. En la primera ingresar los nombres de
empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados
de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000
(tanto el sueldo como su nombre)"""

empleados = []
sueldos = []
cantidad = int(input("Cuantos empleados tiene la empresa? "))
for x in range(cantidad):
    nombre = input("ingrese el nombre del empleado ")
    empleados.append(nombre)
    sueldo = int(input("Ingrese el sueldo del empleado "))
    sueldos.append(sueldo)
for x in range(len(sueldos)):
    print(empleados[x], sueldos[x])


x=0
while x < len(sueldos):
    if sueldos[x] > 10000:
        del(sueldos[x])
        del(empleados[x])
    else:
        x+=1

for x in range(len(sueldos)):
    print(empleados[x],sueldos[x])

#-----------------------------------------------------------------------

""" #108 Crear una lista de 5 enteros y cargarlos por teclado. Borrar los
elementos mayores o iguales a 10 y generar una nueva lista con dichos valores."""

lista = []
for x in range(5):
    numero = int(input("Ingrese un valor "))
    lista.append(numero)
print(lista)

x=0
lista2=[]
while x <len(lista):
    if lista[x]>= 10:
        lista2.append(lista.pop(x))
    else:
        x+=1
print("Lista modificada ", lista)
print("Lista de eliminados ", lista2)

#---------------------------------------------------------------------

"""                      PROGRAMACION ESTRUCTURADA

#109 Confeccionar una aplicación que muestre una presentación en pantalla
del programa. Solicite la carga de dos valores y nos muestre la suma. Mostrar
finalmente un mensaje de despedida del programa.
Implementar estas actividades en tres funciones."""

def presentacion():
    print("Aquí comienza el programa")

def carga_suma():
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    suma = numero1 + numero2
    print("Suma = ", suma)

def finalizacion():
    print("Aquí concluye el programa")

def barra():
    print("------------------------------------------------------------")



presentacion()
carga_suma()
finalizacion()
barra()

#----------------------------------------------------------------------------

""" #110 Confeccionar una aplicación que solicite la carga de dos valores
enteros y muestre su suma.
Repetir la carga e impresion de la suma 5 veces.
Mostrar una línea separadora después de cada vez que cargamos dos valores
y su suma."""

def carga_y_suma():
    numero1 =int(input("Ingrese un valor: "))
    numero2 =int(input("Ingrese un valor: "))
    suma = numero1 + numero2
    print("La suma de los valores es ", suma)

def barra_separadora():
    print("---------------------------------------")

for x in range(5):
    carga_y_suma()
    barra_separadora()

#----------------------------------------------------------------------------

""" #111 Desarrollar un programa con dos funciones. La primer solicite el
ingreso de un entero y muestre el cuadrado de dicho valor. La segunda que
solicite la carga de dos valores y muestre el producto de los mismos. LLamar
desde el bloque del programa principal a ambas funciones.!"""

def cuadrado():
    numero=int(input("Ingrese un numero: "))
    resultado = numero * numero
    print("El numero ingresado elevado al cuadrado es: ", resultado)

def producto():
    numero1=int(input("Ingrese un numero: "))
    numero2=int(input("Ingrese un numero: "))
    resultado = numero1 * numero2
    print("El producto de ambos numeros es: ", resultado)


cuadrado()
producto()

#----------------------------------------------------------------------------

""" #112 Desarrollar un programa que solicite la carga de tres valores y
muestre el menor. Desde el bloque principal del programa llamar 2 veces a
dicha función (sin utilizar una estructura repetitiva)"""

def buscar_menor():
    numero1=int(input("Ingrese el primer numero: "))
    numero2=int(input("Ingrese el primer numero: "))
    numero3=int(input("Ingrese el primer numero: "))
    if numero1<numero2 and numero1<numero3:
        print("Numero menor: ", numero1)
    else:
        if numero2<numero1 and numero2<numero3:
            print("Numero menor: ", numero2)
        else:
            print("Numero menor: ", numero3)


buscar_menor()
buscar_menor()

#--------------------------------------------------------------------------
""" #113 Confeccionar una aplicación que muestre una presentación en
pantalla del programa. Solicite la carga de dos valores y nos muestre
la suma. Mostrar finalmente un mensaje de despedida del programa."""

def mostrar_mensaje(mensaje):
    print(mensaje)
    print("----------------------------------")

def cargar_sumar():
    numero1= int(input("Ingrese un valor: "))
    numero2= int(input("Ingrese un valor: "))
    suma= numero1 + numero2
    print("Suma = ", suma)

mostrar_mensaje("El programa suma dos valores ingresados")
cargar_sumar()
mostrar_mensaje("Fin del programa")

#---------------------------------------------------------------------

""" #114 Confeccionar una función que reciba tres enteros y nos muestre el
mayor de ellos. La carga de los valores hacerlo por teclado. """

def buscar_mayor(num1, num2, num3):
    print("El numero mayor es ")
    if num1>num2 and num1>3:
        print(num1)
    else:
        if num2>num1 and num2>num3:
            print(num2)
        else:
            print(num3)

def cargar_valores():
    numero1=int(input("Ingrese un numero "))
    numero2=int(input("Ingrese un numero "))
    numero3=int(input("Ingrese un numero "))
    buscar_mayor(numero1, numero2, numero3)


cargar_valores()

#----------------------------------------------------------------------------

""" #115 Desarrollar un programa que permita ingresar el lado de un cuadrado.
Luego preguntar si quiere calcular y mostrar su perímetro o su superficie."""

def calcular_perimetro(l1):
    perimetro = l1 * 4
    print("El perimetro del cuadrado es ", perimetro)

def calcular_superficie(lado1):
    superficie = lado1 * lado1
    print("La superficie del cuadrado es ", superficie)

def elegir_calculo():
    lado = int(input("Ingrese el lado de un cuadrado: "))
    eleccion= input("Ingrese p para calcular perimetro o s para superficie ")
    if eleccion == "p":
        calcular_perimetro(lado)
    else:
        if eleccion == "s":
            calcular_superficie(lado)
        else:
            print("La opcion ingresada no es correcta")


elegir_calculo()

#---------------------------------------------------------------------------------
""" #116 Desarrollar una funcion que reciba un string como parametro y
nos muestre la cantidad de vocales. Llamarla desde el bloque principal
del programa 3 veces con string distintos."""


def calcular_vocales(palabra):
    cantidad = 0
    for x in range(len(palabra)):
        if palabra[x] == "a" or palabra[x] == "e" or palabra[x] == "i" or palabra[x] == "o" or palabra[x] == "u":
            cantidad+=1
    print("La palabra ", palabra, " tiene cantidad de vocales: ", cantidad)


calcular_vocales("texto")
calcular_vocales("canguro")
calcular_vocales("editorial")

#----------------------------------------------------------------------------------

""" #117 Confeccionar una función que reciba tres enteros y los muestre
ordenados de menor a mayor. En otra función solicitar la carga de 3 enteros
por teclado y proceder a llamar a la primer función definida."""

def ordenar_enteros(ent1, ent2, ent3):
    if ent1 < ent2 and ent1 < ent3:
        if ent2 < ent3:
            print(ent1, ent2, ent3)
        else:
            print(ent1, ent3, ent2)
    else:
        if ent2 < ent1 and ent2 < ent3:
            if ent1 < ent3:
                print(ent2, ent1, ent3)
            else:
                print(ent2, ent3, ent1)
        else:
            if ent3 < ent1 and ent3 < ent2:
                if ent2 < ent1:
                    print(ent3, ent2, ent1)
                else:
                    print(ent3, ent1, ent2)
                    

def cargar_enteros():
    num1=int(input("Ingrese el primer numero "))
    num2=int(input("Ingrese el siguiente numero "))
    num3=int(input("Ingrese el siguiente numero "))
    ordenar_enteros(num1, num2, num3)


cargar_enteros()

#------------------------------------------------------------------------------

""" #118 Confeccionar una función que le enviemos como parámetro el valor
del lado de un cuadrado y nos retorne su superficie."""

def calcular_superficie(lado_cuadrado):
    superficie = lado_cuadrado * lado_cuadrado
    return superficie


lado = int(input("Ingrese el lado del cuadrado "))
print("La superficie del cuadrado es ", calcular_superficie(lado))

#------------------------------------------------------------------

if calcular_superficie(lado) == 100:
    print("La superficie de este cuadrado es 100")
else:
    print("La superficie de este cuadrado no es 100")

#-----------------------------------------------------------------------------

""" #119 Confeccionar una función que le enviemos como parámetros dos
enteros y nos retorne el mayor."""

def calcular_mayor(num1, num2):
    if num1>num2:
        return num1
    else:
        return num2

numero1 = int(input("Ingrese el primer numero "))
numero2 = int(input("Ingrese el siguiente numero "))
mayor = calcular_mayor(numero1, numero2)
print("El numero mayor es ", mayor)

#-------------------------------------------------------------------------------

""" #120 Confeccionar una función que le enviemos como parámetro un string
y nos retorne la cantidad de caracteres que tiene. En el bloque principal
solicitar la carga de dos nombres por teclado y llamar a la función dos veces.
Imprimir en el bloque principal cual de las dos palabras tiene más caracteres."""


def calcular_caracteres(texto):
    return len(texto)

nombre1 = input("Ingrese el primer nombre ")
nombre2 = input("Ingrese el siguiente nombre ")
print("Palabra con más caracteres")
if calcular_caracteres(nombre1) > calcular_caracteres(nombre2):
    print(nombre1)
else:
    print(nombre2)

#-------------------------------------------------------------------------------

""" #121 Elaborar una función que reciba tres enteros y nos retorne el
valor promedio de los mismos."""

def calcular_promedio(num1, num2, num3):
    promedio = (num1 + num2 + num3) / 3
    return promedio

numero1 = int(input("Ingrese el primer numero "))
numero2 = int(input("Ingrese el siguiente numero "))
numero3 = int(input("Ingrese el siguiente numero "))
promedio = calcular_promedio(numero1, numero2, numero3)
print("El promedio de los valores es ", promedio)

#----------------------------------------------------------------------------

""" #122 Elaborar una función que nos retorne el perímetro de un cuadrado
pasando como parámetros el valor de un lado."""

def calcular_perimetro(valor):
    perimetro = valor * 4
    print("El perimetro del cuadrado es ", perimetro)
    return perimetro

def ingresar_lado():
    lado = int(input("Ingrese el lado del cuadrado "))
    calcular_perimetro(lado)
   
ingresar_lado()

#-------------------------------------------------------------
""" #123 Confeccionar una función que calcule la superficie de un rectángulo y
la retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos
y luego mostrar cual de los dos tiene una superficie mayor"""

def calcular_superficie(lado1, lado2):
    superficie = lado1 * lado2
    return superficie

largo = int(input("Ingrese el largo del primer rectángulo: "))
ancho = int(input("Ingrese el ancho del primer rectángulo: "))
largo2 = int(input("Ingrese el largo del segundo rectángulo: "))
ancho2 = int(input("Ingrese el ancho del segundo rectángulo: "))
if calcular_superficie(largo, ancho) > calcular_superficie(largo2, ancho2):
    print("El primer rectangulo tiene mayor superficie: ", calcular_superficie(largo, ancho))
else:
    print("El segundo rectangulo tiene mayor superficie: ", calcular_superficie(largo2, ancho2))
                                                    
#-----------------------------------------------------------------

""" #124 Plantear una función que reciba un string en mayúsculas o minúsculas
y retorne la cantidad de letras 'a' o 'A'."""

def calcular_letras(tx):
    cantidad = 0
    for x in range(len(tx)):
        if tx[x]=="a" or tx[x] == "A":
            cantidad+=1
    return cantidad
        
texto = input("Ingrese un texto ")
print("El texto tiene ", calcular_letras(texto), "letras a")

#------------------------------------------------------------

""" #125 Definir por asignación una lista de enteros en el bloque principal
del programa. Elaborar tres funciones, la primera recibe la lista y retorna
la suma de todos sus elementos, la segunda recibe la lista y retorna el mayor
valor y la última recibe la lista y retorna el menor."""

def calcular_suma(lista):
    suma= 0
    for x in range(len(lista)):
        suma+=lista[x]
    return suma

def calcular_mayor(lista):
    mayor= lista[0]
    for x in range(1, len(lista)):
        if lista[x]>mayor:
            mayor=lista[x]
    return mayor

def calcular_menor(lista):
    menor= lista[0]
    for x in range(1, len(lista)):
        if lista[x]<menor:
            menor=lista[x]
    return menor
        

lista = [25, 7, 77]
print("Lista original ", lista)
print("Suma ",calcular_suma(lista))
print("El numero mayor es ", calcular_mayor(lista))
print("El numero menor es ", calcular_menor(lista))

#----------------------------------------------------------

""" #126 Crear y cargar por teclado en el bloque principal del programa una
lista de 5 enteros. Implementar una función que imprima el mayor y el menor
valor de la lista."""

def calcular_mayor_menor(lista):
    mayor=lista[0]
    menor=lista[0]
    for x in range(1, len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]
        else:
            if lista[x]<menor:
                menor=lista[x]
    print("Mayor ", mayor)
    print("Menor ", menor)
    

lista=[]
for x in range(5):
    numero = int(input("Ingrese un numero para agregar a la lista "))
    lista.append(numero)
print("Lista ", lista)
calcular_mayor_menor(lista)

#-----------------------------------------------------------------------

""" #127 Crear una lista de enteros por asignación. Definir una función que
reciba una lista de enteros y un segundo parámetro de tipo entero. Dentro de
la función mostrar cada elemento de la lista multiplicado por el valor entero
enviado.
lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)"""


def calcular_producto_lista(lista, num):
    for x in range(len(lista)):
        producto = lista[x]*num
        print(producto)
            
        
lista= [7, 25, 5, 77, 11]
print("Lista original ", lista)
print("Elementos multiplicados por 3")
calcular_producto_lista(lista, 3)

#----------------------------------------------------------

""" #128 Desarrollar una función que reciba una lista de string y nos retorne
el que tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres
debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))"""

def calcular_mas_caracteres(lista):
    mayor = 0
    for x in range(1, len(lista)):
        if len(lista[x]) > len(lista[mayor]):
            mayor= x
    return lista[mayor]

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Lista original ", palabras)
print("Elemento con mas caracteres:", calcular_mas_caracteres(palabras))

#-----------------------------------------------------------------------

""" #129 Definir una lista de enteros por asignación en el bloque principal.
Llamar a una función que reciba la lista y nos retorne el producto de todos
sus elementos. Mostrar dicho producto en el bloque principal de nuestro
programa."""

def calcular_producto(lista):
    producto=1
    for x in range(len(lista)):
        producto *= lista[x]
    return producto

lista = [4, 11, 77, 5, 7]
print("Lista original ", lista)
print("producto de todos los elementos ", calcular_producto(lista))

#--------------------------------------------------------------------

""" #130 Confeccionar una función que cargue por teclado una lista de 5 enteros
y la retorne. Una segunda función debe recibir una lista y mostrar todos los
valores mayores a 10. Desde el bloque principal del programa llamar a ambas
funciones."""


def una_lista():
    lis = []
    for x in range(5):
        numero = int(input("Ingrese un numero "))
        lis.append(numero)
    return lis

def calcular_mayores_diez(li):
    print("Elementos mayores a diez")
    for x in range(len(li)):
        if li[x] > 10:
            print(li[x])

# se le asigna una variable porque si se invoca a la funcion el dato que
#retorna, se pierde.

lista = una_lista()
calcular_mayores_diez(lista)

#---------------------------------------------------------------------
""" #131 Confeccionar una función que cargue por teclado una lista de 5 enteros
y la retorne. Una segunda función debe recibir una lista y retornar el mayor y
el menor valor de la lista. Desde el bloque principal del programa llamar a
ambas funciones e imprimir el mayor y el menor de la lista."""

def cargar_lista():
    lst=[]
    for x in range(5):
        numero = int(input("Ingrese un numero "))
        lst.append(numero)
    return lst


def calcular_mayor_menor(lis):
    mayor= lis[0]
    menor = lis[0]
    for x in range(1, len(lis)):
        if lis[x] > mayor:
            mayor=lis[x]
        else:
            if lis[x]<menor:
                menor=lis[x]
    return[menor, mayor] #retorna una lista

lista= cargar_lista()
mym = calcular_mayor_menor(lista) #se asigna una variable a la lista q retorna
print("Lista: ", lista)
print("Elemento menor:", mym[0])
print("Elemento mayor: ", mym[1])

#---------------------------------------------------------------------

""" #132 Desarrollar un programa que permita cargar 5 nombres de personas y sus
edades respectivas. Luego de realizar la carga por teclado de todos los datos
imprimir los nombres de las personas mayores de edad (mayores o iguales a 18
años). Imprimir la edad promedio de las personas"""

def cargar_nombres():
    nmbrs = []
    edds = []
    for x in range(5):
        nombre = input("Ingrese un nombre ")
        edad = int(input("Ingrese las edad "))
        nmbrs.append(nombre)
        edds.append(edad)
    return [nmbrs, edds]

def mayores_edad(nombres, edades):
    print("Personas mayores de edad:")
    for x in range(len(edades)):
        if edades[x] >= 18:
            print(nombres[x])


def calcular_promedio(edades):
    suma = 0
    for x in range(len(edades)):
        suma += edades[x]
        promedio = suma // 5
    print("El promedio de edades es ", promedio)


nombres, edades = cargar_nombres() #distribuye las listas en 2 variables
mayores_edad(nombres, edades)
calcular_promedio(edades)


#------------------------------------------------------------------

""" #133 En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio."""
superior = 4000
sueldos = []
promedio = 0
def cargar_sueldos():
    for x in range(10):
        sueldo= int(input("Ingrese el sueldo del empleado "))
        sueldos.append(sueldo)
    print("Sueldos: ", sueldos)
    

def calcular_sueldo_mayor(li):
    cantidad = 0
    for x in range(len(li)):
        if li[x] > superior:
            cantidad+=1
    return cantidad


def calcular_promedio(li):
    suma= 0
    for x in range(len(li)):
        suma+= li[x]
        promedio = suma / len(li)
    return promedio 


def calcular_sueldos_inferiores(li):
    print("Sueldos por debado del valor promedio")
    for x in range(len(li)):
        if li[x] < calcular_promedio(li):
            print(li[x])
            

cargar_sueldos()
print("Sueldos superiores a 4000: ", calcular_sueldo_mayor(sueldos))
print("Valor promedio de todos los sueldos ", calcular_promedio(sueldos))
calcular_sueldos_inferiores(sueldos)

#--------------------------------------------------------------------

""" #134 Desarrollar una aplicación que permita ingresar por teclado los
nombres de 5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de articulos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado."""

articulos = []
precios = []

def cargar_articulos(articulos, precios):
    for x in range(5):
        articulo = input("Ingrese el articulo ")
        precio = int(input("Ingrese el precio del articulo "))
        articulos.append(articulo)
        precios.append(precio)
    return [articulos, precios]


def imprimir_productos(articulos, precios):
    for x in range(len(precios)):
        print(articulos[x], precios[x])


def calcular_precio_mayor(articulos, precios):
    mayor = precios[0]
    posicion = 0
    for x in range(1, len(precios)):
        if precios[x] > mayor:
            mayor = precios[x]
            posicion = x
    print("Articulo mas caro ", articulos[posicion], precios[posicion])


def mostrar_articulos(articulos, precios):
    importe = int(input("Ingrese un importe "))
    print("Articulos con valor menor o igual al ingresado:")
    for x in range(len(precios)):
        if precios[x] <= importe:
            print(articulos[x], precios[x])


productos = cargar_articulos(articulos, precios)
imprimir_productos(articulos, precios)
calcular_precio_mayor(articulos,precios)
mostrar_articulos(articulos, precios)

#-------------------------------------------------------------------

""" #135 Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas. """

def cargar_lista():
    lista = []
    for  x in range(10):
        numero = int(input("Ingrese un numero: "))
        lista.append(numero)
    return lista

def separar_elementos(lista):
    lista_negativa = []
    lista_positiva = []
    for x in range(10):
        if lista[x] < 0:
            lista_negativa.append(lista[x])
        else:
            lista_positiva.append(lista[x])
    return [lista_negativa, lista_positiva]

def imprimir_lista(lista):
    for x in range(len(lista)):
        print(lista[x])
    
#-----------------------------------------------------------

        #  FUNCION CON PARAMETRO CON VALOR POR DEFECTO

""" #136 Confeccionar una función que reciba un string como parámetro y en forma
opcional un segundo string con un caracter. La función debe mostrar el string
subrayado con el caracter que indica el segundo parámetro. """

def subrayar_palabra(texto, caracter="="):
    print(caracter*len(texto))
    print(texto)
    print(caracter*len(texto))


subrayar_palabra("Bienvenido al juego")

#-----------------------------------------------------------------------

""" #137 Confeccionar una función que reciba entre 2 y 5 enteros.
La misma nos debe retornar la suma de dichos valores. Debe tener tres
parámetros por defecto."""


def suma_enteros(num1, num2, num3 = 0, num4=0, num5=0):
    suma = num1 + num2 + num3 + num4 + num5
    return suma


print("2 + 4 + 9 + 165412 = ", suma_enteros(2,4,9, 165412))

#--------------------------------------------------------------

""" #138 Confeccionar una función que reciba el nombre de un operario,
el pago por hora y la cantidad de horas trabajadas. Debe mostrar su sueldo
y el nombre. Hacer la llamada de la función mediante argumentos nombrados. """

def calcular_sueldo(operario, costo_hora, cant_horas):
    sueldo = costo_hora * cant_horas
    print(operario, " trabajó ", cant_horas, " horas y su sueldo es de $", sueldo)


calcular_sueldo("Juan", 1500, 18)
calcular_sueldo(cant_horas=15, costo_hora= 2000, operario = "Olivia") 

#----------------------------------------------------









