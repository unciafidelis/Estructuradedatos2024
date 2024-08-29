"""Considera una universidad se con ocen los 50 calificaciones
de un grupo de 50 alumnos. se necesita saber ccuantos de estos 
tienen calificacion superior al promedio del grupo"""

import random

cal = 0
prom = 0
for x in range(1,50):
    cal = random.randint(1,100)
    prom += cal
prom = prom/50
print(f"El promedio es, {prom}")
for x in range(1,50):    
    cal = random.randint(1,100)
    if cal > prom:
        print(cal)

