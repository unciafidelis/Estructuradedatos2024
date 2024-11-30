grafo = [
    [0, 1, 4, float('inf')],
    [float('inf'), 0, 2, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

def warshall(grafo):
    n = len(grafo) 
    cierre = [[1 if grafo[i][j] != float('inf') else 0 for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if cierre[i][j] == 0:
                    cierre[i][j] = cierre[i][k] and cierre[k][j]

    return cierre


print("Algoritmo de Warshal:")
resultado_w = warshall(grafo)
for fila in resultado_w:
    print(fila)