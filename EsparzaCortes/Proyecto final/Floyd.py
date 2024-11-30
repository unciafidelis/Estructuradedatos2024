grafo = [
    [0, 1, 4, float('inf')],
    [float('inf'), 0, 2, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]


# Algoritmo de Floyd
def floyd(matriz):
    n = len(matriz)
    distancias = [fila[:] for fila in matriz]  # Crear una copia de la matriz original

    for intermedio in range(n):
        for origen in range(n):
            for destino in range(n):
                if distancias[origen][intermedio] + distancias[intermedio][destino] < distancias[origen][destino]:
                    distancias[origen][destino] = distancias[origen][intermedio] + distancias[intermedio][destino]

    return distancias


print("Resultados del algoritmo de Floyd:")
resultado = floyd(grafo)
for fila in resultado:
    print(fila)
