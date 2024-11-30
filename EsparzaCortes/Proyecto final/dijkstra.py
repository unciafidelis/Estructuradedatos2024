grafo = [
    [0, 1, 4, float('inf')],
    [float('inf'), 0, 2, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]


def dijkstra(grafo, inicio):
    n = len(grafo)  # Número de nodos
    costos = [float('inf')] * n  # Lista para almacenar los costos mínimos
    procesados = [False] * n  # Lista para saber qué nodos ya se procesaron
    costos[inicio] = 0  # El costo al nodo inicial es 0
    ruta = []  # Lista para seguimiento de los nodos procesados

    ruta.append(inicio)

    for _ in range(n - 1):
        minimo = float('inf')
        nodo_actual = -1
        for i in range(n):
            if not procesados[i] and costos[i] < minimo:
                minimo = costos[i]
                nodo_actual = i

        ruta.append(nodo_actual)
        procesados[nodo_actual] = True

        for vecino in range(n):
            if grafo[nodo_actual][vecino] != float('inf'):
                nuevo_costo = costos[nodo_actual] + grafo[nodo_actual][vecino]
                if nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
    return costos


print("Resultados del algoritmo de Dijkstra:")
print(dijkstra(grafo, 0))
