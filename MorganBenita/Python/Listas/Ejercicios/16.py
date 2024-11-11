class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Valor del nodo
        self.siguiente = None  # Referencia al siguiente nodo

class Cola:
    def __init__(self):
        self.frente = None  # Referencia al primer nodo
        self.ultimo = None  # Referencia al último nodo

    # Encolar: Insertar un nuevo elemento al final de la cola
    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)  # Creamos el nuevo nodo
        if self.ultimo is None:  # Si la cola está vacía
            self.frente = self.ultimo = nuevo_nodo  # El nuevo nodo es tanto el primero como el último
        else:
            self.ultimo.siguiente = nuevo_nodo  # El último nodo apunta al nuevo nodo
            self.ultimo = nuevo_nodo  # Actualizamos el último nodo

    # Desencolar: Eliminar el primer elemento de la cola
    def desencolar(self):
        if self.frente is None:  # Si la cola está vacía
            print("La cola está vacía.")
            return None
        dato = self.frente.dato  # Guardamos el dato a retornar
        self.frente = self.frente.siguiente  # El frente se mueve al siguiente nodo
        if self.frente is None:  # Si la cola quedó vacía
            self.ultimo = None  # No hay último nodo
        return dato

    # Verificar si la cola está vacía
    def esta_vacia(self):
        return self.frente is None  # Si el frente es None, la cola está vacía

    # Ver el primer elemento (sin eliminarlo)
    def ver_frente(self):
        if self.frente is None:
            print("La cola está vacía.")
            return None
        return self.frente.dato

    # Mostrar la cola
    def mostrar(self):
        if self.frente is None:
            print("La cola está vacía.")
            return
        actual = self.frente
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
cola = Cola()

# Encolar elementos
cola.encolar(10)
cola.encolar(20)
cola.encolar(30)

# Mostrar la cola
print("Contenido de la cola:")
cola.mostrar()  # Esperado: 10 -> 20 -> 30 -> None

# Desencolar un elemento
print(f"Elemento desencolado: {cola.desencolar()}")  # Esperado: 10
cola.mostrar()  # Esperado: 20 -> 30 -> None

# Ver el primer elemento
print(f"Primer elemento de la cola: {cola.ver_frente()}")  # Esperado: 20

# Desencolar el resto de los elementos
print(f"Elemento desencolado: {cola.desencolar()}")  # Esperado: 20
print(f"Elemento desencolado: {cola.desencolar()}")  # Esperado: 30
cola.mostrar()  # Esperado: La cola está vacía.
