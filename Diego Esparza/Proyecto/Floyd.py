grafo = [
    [0, 1, 4, float('inf')],
    [float('inf'), 0, 2, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]


#Algoritmo de Floyd
def floyd(grafo):
    n = len(grafo)
    dist = [fila[:] for fila in grafo] 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


    return dist


print("Floyd:")
resultado_fw = floyd(grafo)
for fila in resultado_fw:
    print(fila)