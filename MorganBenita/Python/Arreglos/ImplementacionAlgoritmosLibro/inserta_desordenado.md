# Algoritmo 4: Inserta_desordenado

El algoritmo inserta un elemento en un arreglo unidimensional desordenado. V es un arreglo
de máximo 100 elementos. N es el número actual de elementos. 

# Pseudocódigo

Y representa el valor a insertar 

Si N < 100
entonces
Hacer N <- N + 1 y V[N] <- Y
si no {No hay espacio en el arreglo}
Escribir "El valor Y no se puede insertar. No hay espacio"
{Fin del condicional del paso 1}

```python
import numpy as np

# Definir el tamaño máximo del arreglo y el número actual de elementos
MAX_SIZE = 100
N = 0  # Inicialmente, el arreglo está vacío

# Crear un arreglo vacío de tamaño máximo
V = np.zeros(MAX_SIZE, dtype=int)  # Asumimos que los elementos a insertar son enteros

# Función para insertar un valor en el arreglo
def insertar_valor(Y):
    global N  # Usamos la variable global N
    if N < MAX_SIZE:
        N += 1
        V[N - 1] = Y  # Insertamos Y en la posición N-1 (base 0)
        print(f"Valor {Y} insertado en la posición {N}.")
    else:
        print("El valor Y no se puede insertar. No hay espacio.")

# Ejemplo de uso
valores_a_insertar = [10, 20, 30, 40, 50]  # Ejemplo de valores a insertar

for valor in valores_a_insertar:
    insertar_valor(valor)

# Mostrar el arreglo y el número actual de elementos
print("Arreglo V después de las inserciones:")
print(V[:N])  # Solo mostrar los elementos insertados
print(f"Número actual de elementos: {N}")
```