import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77", database="administracion")

cursor1=conexion1.cursor()

cursor1.execute("select numero, documento, nombre, saldo from cuentas")

for fila in cursor1:
    print(fila)

print("-------------------------------------------------------------------")

cursor1.execute("""update cuentas set nombre='Luis Paez' where numero=00000008 """)
conexion1.commit()

cursor1.execute("select numero, documento, nombre, saldo from cuentas")
for fila in cursor1:
    print(fila)

conexion1.close()