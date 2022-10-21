from persona import Persona
from deportista import Deportista

class Futbolista(Persona,Deportista):
    listajugadores = list()

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listajugadores.append(self)

#metodos get 
    def getGolesMarcados(self):
        return self._golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

#metodos sett

    def setGolesMarcados(self,golesMarcados):
        self._golesMarcados = golesMarcados

    def setTarjetasRojas(self,tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas
    
    def setPiernaHabil(self,piernaHabil):
        self._piernaHabil = piernaHabil

    def __str__(self):
        return f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"


    @classmethod
    def setListaFutbolista(clc, listaFutbolistas):
        clc.listaFutbolistas = listaFutbolistas

  
    def getListaFutbolista(clc):
        return clc.listatoFutbolistas


    