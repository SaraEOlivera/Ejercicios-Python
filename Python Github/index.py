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







