class deportista():
    def __init__(self, añosPracticando):
        self._deporte = "Futbol"
        self._añosPracticando = añosPracticando

    
    #metodos get 
    def getDeporte(self):
        return self._deporte

    def getAñosPracticando(self):
        return self._añosPracticando

    #metodos set 

    def setDeporte(self,deporte):
        self._deporte = deporte

    def setAñosPracticando(self,añosPracticando):
        self._añosPracticando = añosPracticando