arreglo = [10, 20, 30, 40, 50]

for i in range(0, len(arreglo)):
    print(f"Elemento de índice {i} es: {arreglo[i]}")

arreglo[2] = 100

print(f"Arreglo modificado: {arreglo}")

suma = 0
for i in range(0, len(arreglo)):
    suma += arreglo[i]

print(f"La suma de los elementos es: {suma}")