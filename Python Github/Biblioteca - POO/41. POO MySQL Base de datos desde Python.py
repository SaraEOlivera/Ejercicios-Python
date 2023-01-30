#Recuperar filas en una tabla

import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77", database="administracion")

cursor1 = conexion1.cursor()

sql = "insert into libros(titulo, autor, editorial, precio) values(%s, %s, %s, %s)"
datos = ("Lolita", "Nabocov", "Septimo Circulo", 43.7)
cursor1.execute(sql, datos)
datos = ("Matilda", "Roald Dahl", "Santillana", 32.1)
cursor1.execute(sql, datos)
datos = ("Mundo Feliz", "Huxley", "Seix-Barral", 18.7)
cursor1.execute(sql, datos)
datos = ("Romeo y Julieta", "Shakespeare", "Libertador", 87.1)
cursor1.execute(sql, datos)
datos = ("Kentukis", "Schewblin", "Penguin", 52.3)
cursor1.execute(sql, datos)

conexion1.commit()
conexion1.close()
