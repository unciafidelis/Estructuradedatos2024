""" 
Profesor: Jorge Alejandro Morgan Benita
Materia: Estructura de Datos
Proyecto: Implementación de Grafos con los algoritmos de Dijkastra, Floyd-Warshall
Alumno: Jesús Everardo Pinedo Delgado.

"""

#Funcion para ingresar el grafo
def ingresa_grafo():
    n = int(input("¿Cuántos puntos consta el programa de entrega?"))

    #Alamacenar el grafo introducido 
    grafo = {}

    #Ingresar los puntos de entrega
    for i in range(n):
        nodo = input(f"Ingrese el nombre del primer punto de entrega {i + 1}:")
        grafo[nodo] = [] #iniciamos la lista de conexiones

    # Asignamos el peso entre los nodos
    while True:
        nodo1 = input("Ingresa el nombre del primer punto de entrega (o 'fin' para terminar)")
        if nodo1 == 'fin' :
            break
        nodo2 = input(f"Ingresa el nombre de segundo punto de entregar ( o 'fin' para terminar)")
        peso = float(input(f"¿Qué distamcia existre entre el punto d eentrega {nodo1} y el punto de entrega {nodo2}:"))
    
    #verificar que los puntos se guardaron correctamente
        if nodo1 in grafo and nodo2 in grafo:
            grafo[nodo1].append((nodo2, peso))
            [nodo2].append((nodo1, peso)) #grafo no dirigido

        else:
            print("error: uno de lo puntos no existe en el grafo")

    return grafo

#mostrar grafo
def imprimir_grafo(grafo):
    print("\n El orden de las entregas es el siguiente:")
    for nodo, conexiones in grafo.items():
        print(f"{nodo}")
        if conexiones:
            for destino, peso in conexiones:
                print(f"- {destino} (peso: {peso})")
        else:
            print(" Sin destino")

#Algoritmo de Dijkstra
def dijkstra(grafo, nodo_inicio): #A la funcion se le introduce los valores del grafo y el nodo inicio
    #inicializamos las variales con cero
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[nodo_inicio] = 0 #igialamos a cero para el inicio
    camino = {nodo: None for nodo in grafo}

    nodos_no_vistados = list(grafo.keys())

    while nodos_no_vistados:
        nodo_actual = None
        for nodo in nodos_no_vistados:
            if nodo_actual is None:
                nodo_actual = nodo
            elif distancias[nodo] < distancias[nodo_actual]:
                nodo_actual

        #Nodos aledaños del nodo presente
        for vecino, peso in grafo[nodo_actual]:
            if vecino in nodos_no_vistados:
                nueva_distancia = distancias[nodo_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    camino[vecino] = nodo_actual
        
        #Contabilizar nodo presente como visitado
        nodos_no_vistados.remove(nodo_actual)

    return distancias, camino

#Generar camino más corto
def reconstruir_camino(camino, nodo_destino):
    ruta = []
    while nodo_destino is not None:
        ruta.append(nodo_destino)
        nodo_destino = camino[nodo_destino]
    return ruta[::-1]

#Algoritmo fw
def floyd_warshall(grafo):
    # Primero convertimos el grafo en una matriz de distancias
    nodos = list(grafo.keys())
    n = len(nodos)
    
    # Inicializamos la matriz de distancias
    distancias = {nodo: {nodo2: float('inf') for nodo2 in nodos} for nodo in nodos}
    
    # La distancia de un nodo a sí mismo es 0
    for nodo in nodos:
        distancias[nodo][nodo] = 0

    # Rellenamos la matriz de distancias con los valores del grafo
    for nodo1 in grafo:
        for nodo2, peso in grafo[nodo1]:
            distancias[nodo1][nodo2] = peso

    # Implementamos el algoritmo de Floyd-Warshall
    for k in nodos:
        for i in nodos:
            for j in nodos:
                if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
    
    return distancias

# Función para imprimir la matriz de distancias
def imprimir_matriz_distancias(distancias):
    print("\nMatriz de distancias más cortas entre los nodos:")
    nodos = list(distancias.keys())
    print("\t" + "\t".join(nodos))  # Encabezado con los nombres de los nodos
    
    for nodo1 in nodos:
        print(f"{nodo1}\t", end="")
        for nodo2 in nodos:
            if distancias[nodo1][nodo2] == float('inf'):
                print("∞", end="\t")
            else:
                print(f"{distancias[nodo1][nodo2]:.2f}", end="\t")
        print()  # Nueva línea al final de cada fila


#funcion principal
# Menú principal
def main():
    while True:
        print("\n--- Menú de Algoritmos de Grafos ---")
        print("1. Dijkstra")
        print("2. Floyd-Warshall")
        print("3. Salir")
        
        
        sel = input("Seleccione una opción (1-4): ")

        if sel == "3":
            break
        
        grafo = ingresa_grafo()
        imprimir_grafo(grafo)
        

        if sel == "1":
            
            nodo_inicio = input("\nIngrese el nodo de inicio para calcular el camino más corto: ")
            nodo_destino = input("Ingrese el nodo de destino para calcular el camino más corto: ")
    
            if nodo_inicio not in grafo or nodo_destino not in grafo:
                print("Error: Uno de los nodos no existe en el grafo.")
                return
    
            # Aplicar el algoritmo de Dijkstra
            distancias, camino = dijkstra(grafo, nodo_inicio)
    
            # Mostrar la distancia más corta y el camino
            print(f"\nLa distancia más corta desde {nodo_inicio} hasta {nodo_destino} es: {distancias[nodo_destino]}")
            ruta = reconstruir_camino(camino, nodo_destino)
            print(f"El camino más corto es: {' -> '.join(ruta)}")

            
        elif sel == "2":
            imprimir_grafo(grafo)  # Mostrar el grafo
            distancias = floyd_warshall(grafo)  # Calcular las distancias más cortas
            imprimir_matriz_distancias(distancias)  # Imprimir la matriz de distancias

        
if __name__ == "__main__":
    main()
