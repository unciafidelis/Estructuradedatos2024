class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []  # Lista para múltiples hijos

class ArbolNArios:
    def __init__(self):
        self.raiz = None

    def insertar(self, padre, valor):
        nuevo_nodo = Nodo(valor)
        if not self.raiz:
            # Si no hay raíz, el nodo insertado se convierte en la raíz
            self.raiz = nuevo_nodo
            print(f"'{valor}' se ha insertado como la raíz del árbol.")
        else:
            # Buscar el nodo padre
            nodo_padre = self.buscar_nodo(self.raiz, padre)
            if nodo_padre:
                nodo_padre.hijos.append(nuevo_nodo)  # Agregar el nuevo nodo a la lista de hijos
                print(f"'{valor}' se ha insertado como hijo de '{padre}'.")
            else:
                print(f"No se encontró el nodo padre '{padre}'.")

    def buscar_nodo(self, nodo, valor):
        if not nodo:
            return None
        if nodo.valor == valor:
            return nodo
        for hijo in nodo.hijos:
            resultado = self.buscar_nodo(hijo, valor)
            if resultado:
                return resultado
        return None

    def mostrar_arbol(self):
        def _mostrar_recursivo(nodo, nivel):
            if nodo:
                print(" " * (nivel * 4) + f"Nivel {nivel}: {nodo.valor}")
                for hijo in nodo.hijos:
                    _mostrar_recursivo(hijo, nivel + 1)

        if not self.raiz:
            print("El árbol está vacío.")
        else:
            _mostrar_recursivo(self.raiz, 0)

    def calcular_lci(self):
        def _lci_recursivo(nodo, profundidad):
            if not nodo:
                return 0
            lci_hijos = sum(_lci_recursivo(hijo, profundidad + 1) for hijo in nodo.hijos)
            return profundidad + lci_hijos

        # Iniciar con profundidad 1 para contar el nivel raíz
        return _lci_recursivo(self.raiz, 1)

    def contar_nodos(self):
        def _contar_nodos_recursivo(nodo):
            if not nodo:
                return 0
            return 1 + sum(_contar_nodos_recursivo(hijo) for hijo in nodo.hijos)

        return _contar_nodos_recursivo(self.raiz)

    def calcular_lcim(self):
        lci = self.calcular_lci()
        total_nodos = self.contar_nodos()
        if total_nodos == 0:
            return 0  # Evitar división por cero
        return lci / total_nodos

# Uso del programa
arbol = ArbolNArios()

while True:
    print("\n--- Menú ---")
    print("1. Insertar nodo")
    print("2. Mostrar árbol")
    print("3. Calcular LCI")
    print("4. Calcular LCIM")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        valor = input("Ingrese el valor del nodo (puede ser letra o número): ")
        padre = input("Ingrese el valor del nodo padre (o deje vacío si es raíz): ")
        if padre.strip() == "":
            arbol.insertar(None, valor)
        else:
            arbol.insertar(padre, valor)
    elif opcion == "2":
        arbol.mostrar_arbol()
    elif opcion == "3":
        print("La longitud del camino interno (LCI) del árbol es:", arbol.calcular_lci())
    elif opcion == "4":
        print("La media de la longitud del camino interno (LCIM) del árbol es:", arbol.calcular_lcim())
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
