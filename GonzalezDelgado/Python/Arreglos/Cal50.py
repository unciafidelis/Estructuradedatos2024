import random

arregloCal = []
prom = 0
i = 0

while i < 50:
    arregloCal.append(random.randint(1,100))
    prom += arregloCal[i]
    i += 1
print(arregloCal)
prom = prom/50
k = 0
j = 0
cont = 0
print(f"El promedio es, {prom}")
for j in arregloCal:
    if j > prom:
        cont+=1
    k += 1
print(cont) 