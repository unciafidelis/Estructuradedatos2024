# Angel Janvier Gonzalez Delgado
# Primer Examen Parcial de Estructura de Datos
# 07/09/2024 v1.0.0

# Definir un Arreglo unidimensional con 5 Elementos
arreglo = [10, 20, 30, 40, 50]

# Recorrer el Arreglo e Imprimir cada Elemento
for i in range(len(arreglo)):
    print("Elemento en índice", i, "es:", arreglo[i])

# Modificar el Tercer elemento del Arreglo
arreglo[2] = 100

# Imprimir el Arreglo Modificado
print("Arreglo modificado:", arreglo)

# Calcular la Suma de todos los Elementos del Arreglo
suma = 0
for i in range(len(arreglo)):
    suma += arreglo[i]

print("La suma de los elementos es:", suma)


# El programa imprime los elementos de un arreglo, modifica el tercer valor,
# lo imprime de nuevo y calcula la suma total de los elementos.