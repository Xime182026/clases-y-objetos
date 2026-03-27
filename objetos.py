"""Mini proyecto: Sistema de gestión de productos
Objetivo

Crear un programa orientado a objetos que permita:

Crear productos
Mostrar productos
Buscar productos
Actualizar precio y stock
Vender productos
Eliminar productos
Conceptos que se trabajan
Clases y objetos
Constructor
Encapsulamiento
Getters y setters
Métodos
Listas de objetos
"""
class SistemaGestiondeproductos:
    def __init__(self):
        self.productos = [ ]    
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("producto agregado satisfactoreamente")

    def mostrar_producto(self):
        print("lista de productos")  
        print("-" *30)
        for producto in    