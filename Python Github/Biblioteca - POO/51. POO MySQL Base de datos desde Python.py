#Crear una base de datos y una tabla dentro de ésta

import mysql.connector
#no se agrega una base de datos existente sino que se crea una nueva
conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77")
cursor1=conexion1.cursor()

sql="create database bd3"
cursor1.execute(sql)

sql="use bd3"
cursor1.execute(sql)

sql=""" create table frutas (
        nombre varchar(30) primary key,
        precio float   
)"""
cursor1.execute(sql)
conexion1.commit()
conexion1.close()


