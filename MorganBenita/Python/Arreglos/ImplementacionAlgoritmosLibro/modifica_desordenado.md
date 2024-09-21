# Algoritmo 1.6

Hacer I = 1
2. Mientras (I <= N) y (X != V[I]) Repetir
I = I + 1
3. {Fin del ciclo del paso 2}
4. Si (l> N) {No se encontró el valor buscado}
entonces
Escribir "El valor X no se encuentra en el arreglo"
si no
Hacer V[I] = Y
5. {Fin del condicional del paso 4}

```python
import numpy as np

# Inicialización del arreglo con un máximo de 100 elementos
V = np.array([25, 12, 34, 47, 58, 63, 12, 22])  # El arreglo puede ser desordenado
N = len(V)  # Número actual de elementos en el arreglo (puede ser menor a 100)
X = 47  # Valor que queremos buscar para modificar
Y = 99  # Valor por el cual se reemplazará si se encuentra
I = 1  # Inicializar I en 1 (siguiendo el pseudocódigo)

# Imprimir el arreglo original
print("Arreglo original:", V)

# Paso 2: Mientras (I <= N) y (X != V[I-1]) Repetir
# Recordemos que en Python los índices comienzan en 0, así que usamos I-1
while I <= N and V[I-1] != X:
    I += 1

# Paso 3: Fin del ciclo

# Paso 4: Si (I > N), significa que no se encontró el valor X
if I > N:
    # Si I es mayor que N, el valor no fue encontrado
    print(f"El valor {X} no se encuentra en el arreglo.")
else:
    # Si se encuentra el valor, reemplazarlo con Y
    V[I-1] = Y  # Usamos I-1 para ajustar al índice de Python
    print(f"El valor {X} fue encontrado y reemplazado por {Y}.")

# Paso 5: Fin del condicional

# Mostrar el arreglo actualizado
print("Arreglo actualizado:", V)

```