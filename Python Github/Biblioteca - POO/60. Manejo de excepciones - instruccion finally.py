#Almacenar una serie de string en un archivo de texto. Tratar de llamar al método 'write' 
# pasando un entero.
try:
    archivo1 = open("attaque.txt","w")
    archivo1.write("Esta es la primera línea del archivo\n")
    archivo1.write("Esta es la siguiente línea del archivo\n")
    archivo1.write(77)
except TypeError:
    print("No se puede agregar en numero entero al metodo write")
finally:
    archivo1.close()
    print("Se cerró el archivo correctamente")

