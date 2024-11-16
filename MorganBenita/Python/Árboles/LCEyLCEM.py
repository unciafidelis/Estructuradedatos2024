class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []  # Lista de hijos

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)  # Añadir hijo sin restricción


class Arboles:
    def __init__(self):
        self.raiz = None
        self.max_hijos = 0  # Se inicializa el número máximo de hijos

    def insertar(self, padre, valor):
        nuevo_nodo = Nodo(valor)
        if not self.raiz:
            self.raiz = nuevo_nodo
            print(f"'{valor}' se ha insertado como la raíz del árbol.")
        else:
            nodo_padre = self.buscar_nodo(self.raiz, padre)
            if nodo_padre:
                nodo_padre.agregar_hijo(nuevo_nodo)
                print(f"'{valor}' se ha insertado como hijo de '{padre}'.")
            else:
                print(f"No se encontró el nodo padre '{padre}'.")
        self.actualizar_max_hijos()  # Actualizamos el máximo número de hijos

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
            _mostrar_recursivo(self.raiz, 1)

    def actualizar_max_hijos(self):
        """Actualiza el número máximo de hijos en el árbol."""
        def _max_hijos_recursivo(nodo):
            if not nodo:
                return 0
            max_hijos = len(nodo.hijos)
            for hijo in nodo.hijos:
                max_hijos = max(max_hijos, _max_hijos_recursivo(hijo))
            return max_hijos
        self.max_hijos = _max_hijos_recursivo(self.raiz)  # Máximo número de hijos

    def agregar_nodos_especiales(self, nodo, nivel):
        """Calcula y agrega nodos especiales por nivel."""
        nivel += 1
        if nivel not in self.nivel_nodos:
            self.nivel_nodos[nivel] = 0
        if len(nodo.hijos) < self.max_hijos:
            nodos_especiales = self.max_hijos - len(nodo.hijos)
            self.nivel_nodos[nivel] += nodos_especiales
        for hijo in nodo.hijos:
            self.agregar_nodos_especiales(hijo, nivel)

    def calcular_LCE(self):
        """Calcula la Longitud del Camino Externo (LCE)."""
        self.nivel_nodos = {}
        self.agregar_nodos_especiales(self.raiz, 1)  # Rellenar nodos especiales

        LCE = 0
        for nivel, cantidad in self.nivel_nodos.items():
            LCE += nivel * cantidad
            print(f"Nivel {nivel}: {cantidad} nodos especiales contribuyen {nivel * cantidad} a LCE.")
        return LCE

    def calcular_LCEM(self, LCE):
        """Calcula la Longitud Media del Camino Externo (LCEM)."""
        total_nodos_especiales = sum(self.nivel_nodos.values())
        if total_nodos_especiales == 0:
            return 0  # Evitar división por cero
        return LCE / total_nodos_especiales


# Uso del programa
arbol = Arboles()

while True:
    print("\n--- Menú ---")
    print("1. Insertar nodo")
    print("2. Mostrar árbol")
    print("3. Calcular LCE")
    print("4. Calcular LCEM")
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
        lce = arbol.calcular_LCE()
        print(f"La Longitud del Camino Externo (LCE) del árbol es: {lce}")
    elif opcion == "4":
        lce = arbol.calcular_LCE()
        lcem = arbol.calcular_LCEM(lce)
        print(f"La Media de la Longitud del Camino Externo (LCEM) del árbol es: {lcem:.2f}")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
