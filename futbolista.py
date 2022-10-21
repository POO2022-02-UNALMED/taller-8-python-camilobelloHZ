from persona import Persona
from deportista import Deportista

class Futbolista(Persona,Deportista):
    listaFutbolistas = list()

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        
        Futbolista.listaFutbolistas.append(self)

    #gett 
    def getGolesMarcados(self):
        return self._golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas


    def getPiernaHabil(self):
        return self._piernaHabil

    #sett
    def setGolesMarcados(self,x):
        self._golesMarcados = x

    def setTarjetasRojas(self,x):
        self._tarjetasRojas = x

    def setPiernaHabil(self,x):
        self._piernaHabil = x

    @classmethod
    def setListaFutbolista(clc, listaFutbolistas):
        clc.listaFutbolistas = listaFutbolistas
    
    @classmethod
    def getListaFutbolista(clc):
        return clc.listadoJugadores


    def __str__(self):
        return f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"
    