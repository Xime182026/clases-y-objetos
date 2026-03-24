#clases 
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
print(perro1.nombre, perro1.edad)