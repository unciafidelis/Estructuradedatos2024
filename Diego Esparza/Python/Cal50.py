"""
Consideremos que en una universidad se conocen las calificaciones de un grupo de 50
alumnos. Se necesita saber cuántos de éstos tienen calificación superior al promedio del
grupo.
¿Cómo resolver este problema?"""

import random
arregoloCal = []
cal = 0
prom = 0
i = 0

while i <= 50:
   
    arregoloCal.append(random.randint(1,100))

    prom += arregoloCal [i]	
    i += 1
print (arregoloCal)    
prom = prom/50

k = 0
j = 0
cont = 0
print(f"el promedio es,{prom}")

for j  in arregoloCal:

   hAFSDFYFDYUWQFDYWQD
   
  
   if  j > prom:
        cont += 1
   k += 1    
print(cont)
   
