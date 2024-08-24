"""Ejercicio de calificaciones de un grupos de 50
alumnoos para conocer cuantos tienen superiori al promedio"""

import random

cal = 0
promedio = 0
i = 0
arregloCal = []

while i < 50:
    cal = random.randint(1, 100)
    arregloCal.append(cal)  
    promedio += arregloCal[i]
    i += 1

promedio = promedio / 50
print(f"El promedio es {promedio}")

i = 0
cont = 0
j=0
for i in arregloCal:
    if i > promedio:
        cont += 1
    j += 1

print(cont)
