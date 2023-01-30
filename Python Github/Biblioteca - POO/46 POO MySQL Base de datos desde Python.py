#Borrado y modificación de filas.

import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77", database="administracion")

cursor1 = conexion1.cursor()
cursor1.execute("select numero, documento, nombre, saldo from cuentas" )
for fila in cursor1:
    print(fila)

print("--------------------------------------------------------------------")

#cursor1.execute("delete from cuentas where numero=00000003")
cursor1.execute("""update cuentas set nombre='Juana' where documento=22555444""")
conexion1.commit()

conexion1.close()
