#Conectarse al servidor y mostrar todas las BBDD existentes.

# 1. importar el conector mysqlconector
import mysql.connector

#2. definir objeto conexion1 que  se crea a traves de mysqulconector 
# llamar funcion conect y pasarle 3 parametros: host=localhost 
# (donde funciona el servidor mysql), user=root y clave vacia en pswd
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="sql77")

#3. crear objto cursor1 a traves del objeto creado conexion1. Llamar al metodo
#cursor que devuelve objeto de la clase cursor
cursor1=conexion1.cursor()

#4  en cursor1, llamar al metodo execute y pasarle comando sql show database 
# que recupera todas las bbdd instaladas en mysql
cursor1.execute("show databases")

#5 recorrer con un for y pasarle cursor1 e imprimir cada nombre de bbdd
# que hay en el servidor
for base in cursor1:
    print(base)

#6 cerrar la conexion
conexion1.close() 