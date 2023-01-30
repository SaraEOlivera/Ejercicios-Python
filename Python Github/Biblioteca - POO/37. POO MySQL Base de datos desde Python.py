# Crear un programa que recupere todas las tablas contenidos en una base de datos. 

# 1. importar el modulo mysqlconector

import mysql.connector

# 2. Crear el objeto conexion1 del modulo mysql.connector  con la funcion connect y pasarle 4 parametros
# host, user, pswd y el nombre de la base de datos

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77", database="administracion")

#3. Crear objeto cursor a traves del objeto creado conexion1. Llamar al metodo
#cursor que devuelve objeto de la clase cursor

cursor1 = conexion1.cursor()

#4  en cursor1, llamar al metodo execute y pasarle comando sql show tables 
# que recupera todas las tablas que tiene la base de datos. 
cursor1.execute("show tables")

#5 recorrer con un for y pasarle cursor1 e imprimir cada nombre de bbdd
# que hay en el servidor

for tabla in cursor1:
    print(tabla)

#6 cerrar la conexion
conexion1.close()

