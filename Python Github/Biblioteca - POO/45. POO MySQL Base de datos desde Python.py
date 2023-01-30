import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77", database="administracion")

cursor1 = conexion1.cursor()

cursor1.execute("select documento, nombre, domicilio, fechaNacimiento from alumnos")

for fila in cursor1:
    print(fila)

conexion1.close()

