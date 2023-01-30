#insertar filas en una tabla

import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77", database="administracion")

cursor1 = conexion1.cursor()

#definir string con el comando sql que se quiere ejecutar. usar mascaras %s
sql="insert into cuentas(documento, nombre, saldo) values(%s, %s, %s)"

#sustituir datos por mascaras a traves de tuplas
datos = (22555444, "Olimanteca", 45000)

# pasarle a la funcion execute los parametros con el comando sql + tupla con datos para reemplazar
#los % con los datos de la tupla
cursor1.execute(sql, datos)

#definir otra tupla con + datos
datos = (11333222, "Juan Perez", 5000)

#volver a llamar a la funcion execute
cursor1.execute(sql, datos)

datos = (33112222, "Bialet Masse", 2000)
cursor1.execute(sql, datos)

datos = (2111212, "Saldan", 4000)
cursor1.execute(sql, datos)

#para que mysql ejecute los comandos llamar metodo commit
conexion1.commit()

conexion1.close()

