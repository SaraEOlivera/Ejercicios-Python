#Recuperar todas las filas de una tabla.

import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77", database="administracion")
cursor1 = conexion1.cursor()

#a execute se le pasa el string con comando sql que se quiere ejecutar
cursor1.execute("select codigo, titulo, autor, editorial, precio from libros")

#recorrer datos devueltos en cursor1:
#en la variable fila se guarda un tupla por cada fila recuperada del comando select
for fila in cursor1:
    print(fila)

conexion1.close()