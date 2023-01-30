#Obtener todas las bases de datos de una tabla.

import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77", database="mydb")

cursor1 = conexion1.cursor()

cursor1.execute("show tables")

for tabla in cursor1:
    print(tabla)

conexion1.close()

