from Dado import *

class Ficha:
    color = ""
    posicion = 0
    nombre = ""

    #no era parte del modelo, pero la Ficha necesita usar un dado
    #este atributo se define cuando definimos relaciones entre clases
    #lo que veremos más adelante en el curso
    dado = Dado(6)
    
    
    def __init__(self, color, nombre):
        self.color = color
        self.posicion = 0
        self.nombre = nombre 
        #self.nombre = nombre 
    
    def avanzar(self):
        #aquí se vuelve claro por qué necesitamos un dado
        pasos = self.dado.lanzar()
        self.posicion += pasos
        print(self.color, " tiró ",  pasos)
        print("El jugador ", self.color, "está en la posición",self.posicion)
    





#jugador = Ficha("Pri", "Pri")



