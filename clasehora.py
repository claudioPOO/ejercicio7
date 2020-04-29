from clasefecha import FechaHora
class Hora:
    __hora=0
    __minutos=0
    __segundos=0
    def __init__(self,h=0,m=0,s=0):
        self.__hora=int(h)
        self.__minutos=int(m)
        self.__segundos=int(s)
    def __str__(self):
        return('%d hs: %d min: %d seg'%(self.__hora,self.__minutos,self.__segundos))
    def getH(self):
        return self.__hora
    def getM(self):
        return self.__minutos
    def getS(self):
        return self.__segundos
    def __radd__(self,hora):
            return FechaHora(hora.getDia(),hora.getMes(),hora.getAño(),self.__hora+hora.getHora(),self.__minutos + hora.getMin(),self.__segundos+ hora.getSeg())     
        
        