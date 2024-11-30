grafo = [
    [0, 1, 4, float('inf')],
    [float('inf'), 0, 2, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]


def cierre_transitivo(matriz):
    n = len(matriz)  # Número de nodos
    alcance = [[1 if matriz[i][j] != float('inf') else 0 for j in range(n)] for i in range(n)]

    for intermedio in range(n):
        for origen in range(n):
            for destino in range(n):
                if alcance[origen][destino] == 0:
                    alcance[origen][destino] = alcance[origen][intermedio] and alcance[intermedio][destino]

    return alcance


print("Resultados del algoritmo de cierre transitivo (Warshall):")
resultado = cierre_transitivo(grafo)
for fila in resultado:
    print(fila)
