arreglo = [10,20,30,40,50]

for i in range(0, len(arreglo)):
    print(arreglo[i])
    
arreglo[2] = 100

print(arreglo)

suma= 0
for i in range(0, len(arreglo)):
    suma += arreglo[i]
    
print("La suma del arreglo es:", suma)