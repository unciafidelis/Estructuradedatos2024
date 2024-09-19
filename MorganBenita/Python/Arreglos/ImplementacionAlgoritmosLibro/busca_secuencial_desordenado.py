import numpy as np

# Definir el tamaño del arreglo (N) y el valor a buscar (X)
N = 10  # Por ejemplo, puedes cambiar este valor
X = 5   # Cambia este valor para buscar diferentes números

# Crear un arreglo de ejemplo con números del 1 al N
V = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Arreglo de ejemplo

# Inicializar la variable auxiliar I
I = 0  # Comenzamos en el índice 0 para el arreglo (en Python)

# Búsqueda del valor X en el arreglo V
while I < N and X != V[I]:
    I += 1

# Evaluar si se encontró el valor
if I >= N:
    print("El valor X no está en el arreglo")
else:
    print(f"El valor X está en la posición {I + 1}")  # Se suma 1 para mostrar la posición en base 1