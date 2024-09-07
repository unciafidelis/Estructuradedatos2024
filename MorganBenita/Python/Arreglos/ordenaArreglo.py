import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [9, 8, 7], [10, 5, 6]])
desordenado = np.array([], dtype=int)
for i in a:
    for j in i:
        desordenado = np.append(desordenado, j)
N = len(desordenado)
i = 0
while i < N:
    j = 0
    while j < N - 1: 
        if desordenado[j] > desordenado[j + 1]:
            desordenado[j], desordenado[j + 1] = desordenado[j + 1], desordenado[j]
        j += 1  
    i += 1  
print("Arreglo ordenado de forma ascendente:")
print(desordenado)
