arreglo = [10, 20, 30, 40, 50]

for i in range(0, len(arreglo)):
    print("Elemento en indice", i, "es:", arreglo[i])
    

arreglo[2] = 100

print("Arreglo modificado:", arreglo)

suma = 0
for i in range(0, len(arreglo)):
    suma = suma + arreglo[i]
print("La suma de los elementos es:", suma)