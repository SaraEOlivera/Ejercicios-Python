"""
Confeccionar una aplicación que permita cargar por teclado una lista de enteros,
obtener y mostrar el mayor y calcular su suma. Definir un módulo con las
funciones de carga, identificar el mayor y sumar. En el módulo principal del
programa importar el otro módulo y llamar a sus funciones.
"""
import operaciones

lista = operaciones.cargarNumeros()
operaciones.calcularMayor(lista)
operaciones.calcularSuma(lista)
