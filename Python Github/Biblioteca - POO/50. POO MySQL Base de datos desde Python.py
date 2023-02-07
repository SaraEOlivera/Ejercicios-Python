#Inserción de múltiples filas en una tabla.

import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77", database="administracion")
cursor1=conexion1.cursor()

sql=("insert into articulos(codigo, nombre, descripcion, precio, cantidad) values(%s, %s, %s, %s, %s)")
datos= [ (6, "auriculares", "inalambricos", 54.0, 200),
         (7, "cable", "cable hdmi", 87.1, 120),
         (8, "impresora", "Epson", 452.2, 100),
         (9, "monitor", "Samsung", 65.87, 50) ]

cursor1.executemany(sql, datos)
conexion1.commit()

conexion1.close()