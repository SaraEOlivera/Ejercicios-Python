#Recuperar filas en una tabla

import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77", database="administracion")

cursor1 = conexion1.cursor()

#definir string con el comandp sql que se quiere ejecutar. usar mascaras %s

sql = "insert into libros(titulo, autor, editorial, precio) values(%s, %s, %s, %s)"

#sustituir mascaras por datos en tupla
datos=("Los dias del venado", "Bodoc", "De Bolsillo", 35.2)

#executar con parametros sql + datos
cursor1.execute(sql, datos)

datos=("Los dias de la sombre", "Bodoc", "De Bolsillo", 27.1)
cursor1.execute(sql, datos)

datos=("Los dias del fuego", "Bodoc", "De Bolsillo", 40.0)
cursor1.execute(sql, datos)

datos=("El Hobbit", "Tolkien", "De Bolsillo", 18.2)
cursor1.execute(sql, datos)

datos=("Saga de los confines", "Bodoc", "De Bolsillo", 95.3)
cursor1.execute(sql, datos)

#para que mysql ejecute los comandos llamar metodo commit
conexion1.commit()

conexion1.close()
