import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="sql77", database="administracion")
cursor1=conexion1.cursor()

cursor1.execute("delete from cuentas where numero=00000009")
cursor1.execute("""update cuentas set nombre='Pedro' where numero=00000010""")
conexion1.commit()

cursor1.execute("delete from cuentas where numero=00000011")
cursor1.execute("""update cuentas set nombre='Luisa Perez' where numero=00000012""")
conexion1.commit()

cursor1.execute("delete from cuentas where numero=00000013")
cursor1.execute("""update cuentas set nombre='Sandra Lopez' where numero=00000014 """)
conexion1.commit()

cursor1.execute("select numero, documento, nombre from cuentas")
for fila in cursor1:
    print(fila)

conexion1.close()