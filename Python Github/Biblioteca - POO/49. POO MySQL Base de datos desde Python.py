import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77", database="administracion")
cursor1 = conexion1.cursor()

sql="insert into medicamentos(nombre, laboratorio, precio, cantidad) values(%s, %s, %s, %s)"
datos=("Febratic", "Rocha", 25.4, 150)
cursor1.execute(sql, datos)

conexion1.commit()
print("Valor del ultimo codigo de articulo generado", cursor1.lastrowid)

conexion1.close()