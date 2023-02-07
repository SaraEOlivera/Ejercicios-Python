#Conectarse a una base de datos de MySQL y ejecutar un comando SQL incorrecto.



import mysql.connector

try:
    conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77")
    cursor1=conexion1.cursor()
    cursor1.execute("show databasessssss")
    for base in cursor1:
        print(base)
except mysql.connector.errors.ProgrammingError:
    print("Error en la base de datos")
finally:
    conexion1.close()
    print("La base de datos se cerró correctamente")

    