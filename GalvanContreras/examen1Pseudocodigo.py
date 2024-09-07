# Definir un arreglo unidimensional con 5 elementos
arreglo = [10, 20, 30, 40, 50]

# Recorrer el arreglo e imprimir cada elemento
for i in range(len(arreglo)):
    print("Elemento en índice", i, "es:", arreglo[i])

# Modificar el tercer elemento del arreglo
arreglo[2] = 100

# Imprimir el arreglo modificado
print("Arreglo modificado:", arreglo)

# Calcular la suma de todos los elementos del arreglo
suma = 0
for i in range(len(arreglo)):
    suma += arreglo[i]

print("La suma de los elementos es:", suma)
