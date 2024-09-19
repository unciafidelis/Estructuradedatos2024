import numpy as np

# Definir el tamaño máximo del arreglo y el número actual de elementos
MAX_SIZE = 100
N = 0  # Inicialmente, el arreglo está vacío

# Crear un arreglo vacío de tamaño máximo
V = np.zeros(MAX_SIZE, dtype=int)  # Asumimos que los elementos son enteros

# Función para insertar valores en el arreglo (para pruebas)
def insertar_valor(Y):
    global N  # Usamos la variable global N
    if N < MAX_SIZE:
        V[N] = Y  # Insertamos Y en la posición N
        N += 1
    else:
        print("No hay espacio para insertar el valor.")

# Función para eliminar un valor del arreglo
def eliminar_valor(X):
    global N  # Usamos la variable global N
    I = 0

    # Buscar el valor X en el arreglo
    while I < N and V[I] != X:
        I += 1

    # Comprobar si se encontró el valor
    if I == N:  # No se encontró el valor
        print("El valor X no se encuentra en el arreglo")
    else:
        # Si se encontró, eliminarlo desplazando los elementos
        for K in range(I, N - 1):  # Desplazar elementos a la izquierda
            V[K] = V[K + 1]
        N -= 1  # Disminuir el número actual de elementos
        print(f"El valor {X} ha sido eliminado del arreglo.")

# Ejemplo de uso
# Insertar algunos valores para probar la eliminación
valores_a_insertar = [10, 20, 30, 40, 50]  # Ejemplo de valores a insertar
for valor in valores_a_insertar:
    insertar_valor(valor)

# Mostrar el arreglo antes de la eliminación
print("Arreglo V antes de la eliminación:")
print(V[:N])  # Solo mostrar los elementos insertados

# Intentar eliminar un valor
valor_a_eliminar = 30
eliminar_valor(valor_a_eliminar)

# Mostrar el arreglo después de la eliminación
print("Arreglo V después de la eliminación:")
print(V[:N])  # Solo mostrar los elementos restantes
