grafo = [
    [0, 1, 4, float('inf')],
    [float('inf'), 0, 2, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]


def dijkstra(grafo, inicio):
    n = len(grafo) 
    distancias = [float('inf')] * n 
    visitados = [False] * n
    distancias[inicio] = 0
    S = []

    S.append(inicio)

    for _ in range(n - 1):
        menor = float('inf')
        nodo = -1
        for i in range(n):
            if not visitados[i] and distancias[i] < menor:
                menor = distancias[i]
                nodo = i

        S.append(nodo)
        visitados[nodo] = True

        for vecino in range(n):
            if grafo[nodo][vecino] != float('inf'):
                nueva_distancia = distancias[nodo] + grafo[nodo][vecino]
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
    return distancias




print("ejecución de algoritmo Dijkstra:")
print(dijkstra(grafo, 0))    