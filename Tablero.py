
from Ficha import *

class Tablero:
    nombreJuego = ""
    dado = None 
    espacios = 0
    jugadores = []
    cantJugadores = 0


    #Defina aquí los atributos de Tablero
    


    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno
    




    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self, nombreJuego, numEspacios):
        self.nombreJuego = nombreJuego
        self.espacios = numEspacios
        self.dado = Dado(6)
        self.jugadores = [Ficha("Azul", "Azul"), Ficha("Rojo", "Rojo")]
        self.cantJugadores = 2 

        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase

    def turno(self): 
        self.jugadores[0].avanzar()
        if self.jugadores[0].posicion >= self.espacios: 
            print("Ganó el jugador ", self.jugadores[0].color)
            return True 
        else: 
            self.jugadores.append(self.jugadores.pop(0))
            return False 

    def juego(self): 
        jugar = True
        while(jugar): 
            resultado = self.turno()
            if(resultado): 
                jugar = False

        
    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self


tablero = Tablero("Battleship", 20)
tablero.juego()