print ("Bienvenido a mi programa")

arreglo = [10, 20, 30, 40, 50]


for i in range(len(arreglo)):
    print(f"Elemento en índice {i} es: {arreglo[i]}")

arreglo[2] = 100


print("Arreglo modificado:", arreglo)


suma = 0
for i in range(len(arreglo)):
    suma += arreglo[i]

print("La suma de los elementos es:", suma)