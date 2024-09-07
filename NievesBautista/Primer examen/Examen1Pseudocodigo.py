"""
Edgar Israel Nieves Bautista
Hacer el pseudocodigo a codigo en python

"""

# Definir un arreglo unidimensional con 5 elementos
arreglo = [10, 20, 30, 40, 50]

#imprimimos cada elemento del arreglo con un for
for i in range(len(arreglo)):
    print("Elemento en índice", i, "es:", arreglo[i])

# Modificar el tercer elemento del arreglo (índice 2)
arreglo[2] = 100

#imprimimos el tercer elemento modificado y el arreglo completo
print("El tercer elemento modificado es:", arreglo[2])

print("Arreglo modificado:", arreglo)

#calculamos la suma con un for
suma = 0
for i in range(len(arreglo)):
    suma += arreglo[i]

print("La suma de los elementos es:", suma)
