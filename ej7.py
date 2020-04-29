from clasefecha import FechaHora
from clasehora import Hora

if __name__ == '__main__':

   d = int(input("Ingrese Dia: "))
   mes = int(input("Ingrese Mes: "))
   a = int(input("Ingrese Año: "))
   h = int(input("Ingrese Hora: "))
   m = int(input("Ingrese Minutos: "))
   s = int(input("Ingrese Segundos: "))
   f = FechaHora(d,mes,a,h, m, s)
   print(f)
   input()
   h1 = int(input("Ingrese Hora: "))
   m1 = int(input("Ingrese Minutos: "))
   s1 = int(input("Ingrese Segundos: "))
   r = Hora(h1,m1,s1)
   print(r)
   input()
   
   f2 = f + r
   print(f2)
   input()
   f3 = r + f
   f3.acomodar()
   print(f3)
   input()
   f4 = f3 - 1
   f4.acomodaR
   print(f4)
   f4 = 1 + f2
   print(f4)
   f4.acomodar()
   input()
       
      
  
