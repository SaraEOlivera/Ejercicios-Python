#Borrar una base de datos.

import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77")

cursor1 = conexion1.cursor()

sql = "drop database if exists bd3"
cursor1.execute(sql)

sql=("create database bd3")
cursor1.execute(sql)

conexion1.close()