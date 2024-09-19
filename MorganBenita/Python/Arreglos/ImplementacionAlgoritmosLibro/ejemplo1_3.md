# Ejemplo 1.3
Sea A un arreglo de 26 elementos booleanos con índices de tipo carácter.

```python
import numpy as np

# Número total de componentes (NTC = 26 para las letras de 'a' a 'z')
NTC = 26

# Crear un arreglo de 26 elementos booleanos con numpy, inicializados como False
A = np.zeros(NTC, dtype=bool)

# Función para mapear un carácter ('a' a 'z') a su índice correspondiente en el arreglo numpy
def char_to_index(char):
    return ord(char) - ord('a')  # 'a' -> 0, 'b' -> 1, ..., 'z' -> 25

# Función para acceder y modificar los elementos con índice de tipo carácter
def set_value(char, value):
    index = char_to_index(char)
    A[index] = value

def get_value(char):
    index = char_to_index(char)
    return A[index]

# Mostrar el arreglo inicial
print("Arreglo A con valores booleanos de 'a' a 'z':")
print(A)

# Modificar todos los valores en el arreglo usando índices de tipo carácter
for char in range(ord('a'), ord('z') + 1):  # Iterar desde 'a' (97) hasta 'z' (122)
    set_value(chr(char), True)  # Asignar True a cada letra

# Mostrar el arreglo modificado
print("Arreglo A modificado:")
print(A)

# Ejemplos de acceso a valores
for char in range(ord('a'), ord('z') + 1):
    print(f"A['{chr(char)}'] hace referencia al elemento de la posición '{chr(char)}': {get_value(chr(char))}")

```