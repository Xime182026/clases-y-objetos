"""#clases 
class perro:
    def _init_(self, nombre, edad): #funciones
        self.nombre  = nombre #
        self.nombre = edad
        
#class 

        
        
class Perro:
    def ladrar(self):
        return "¡Guau!"
    def rascarse(self):
        print("Me estoy rascando" )
        
perro1 = perro("roki", 5)
perrito = Perro("firulais" , 3)
print(perro1.nombre, perro1.edad)"""

class Galleta:
    def __init__ (self, sabor, forma, tamaño, color, precio):
        self.sabor = sabor
        self.forma = forma
        self.tamaño = tamaño
        self.color = color
        self.precio = precio
    
    def hornear(self):
        print("La galleta se está horneando.")
    def decorar(self):
        print("La galleta se está decorando.")
    def comer(self):
        print("La galleta se está comiendo.")
    
    def __repr__(self):
        return (f"Galleta: Forma: {self.forma}, Sabor: {self.sabor} "
                f"Tamaño: {self.tamaño}, Color: {self.color}, Precio: ${self.precio}")
        
galleta1 = Galleta("Chocolate", "Redonda", "Mediana", "Marrón", 1.50)
galleta1.comer()
galleta1.hornear()
print(galleta1)

"""
ejericicio sistema de biblioteca
clase libro
atributos:
    
titulo(str)
autor (str)
paginas(int)
prestado(bool) incialmente en False
metodos:
prestar(): cambia el estado de prestado a True y muestra un mensaje indicando 
que el libro ha sido prestado.
devolver(): cambia el estado de prestado a False y muestra un mensaje indicando 
que el libro ha sido devuelto.
resumen():imprime titulo, autor y paginas
estado(): muestra si el libro está prestado o disponible"""

class Libro:
    def __init__ (self, titulo :str , autor , paginas ):
        self. titulo = titulo
        self. autor = autor
        self. paginas = paginas

    def prestar(self):
        print ("El libro a sido prestado")

    def devolver(self):
        print("El libro a sido devuelto")
    
    def resumen(self):
        print()