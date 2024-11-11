class Cola:
    def __init__(self):
        self.cola = []  # Inicializamos la cola como una lista vacía

    # Insertar un elemento en la cola
    def encolar(self, elemento):
        self.cola.append(elemento)

    # Eliminar un elemento de la cola (FIFO)
    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            print("La cola está vacía.")
            return None

    # Verificar si la cola está vacía
    def esta_vacia(self):
        return len(self.cola) == 0

    # Mostrar el contenido de la cola
    def mostrar_cola(self):
        if not self.esta_vacia():
            print("Contenido de la cola:", self.cola)
        else:
            print("La cola está vacía.")

    # Eliminar elementos repetidos en la cola
    def eliminar_repetidos(self):
        elementos_vistos = set()  # Conjunto para rastrear elementos ya vistos
        cola_sin_repetidos = []  # Lista que almacenará la cola sin repeticiones

        for elemento in self.cola:
            if elemento not in elementos_vistos:
                cola_sin_repetidos.append(elemento)  # Agregamos el elemento si no ha sido visto antes
                elementos_vistos.add(elemento)  # Marcamos el elemento como visto

        self.cola = cola_sin_repetidos  # Actualizamos la cola original sin repetidos

# Ejemplo de uso

# Crear una instancia de la cola
mi_cola = Cola()

# Encolar elementos, incluyendo algunos repetidos
mi_cola.encolar(1)
mi_cola.encolar(2)
mi_cola.encolar(3)
mi_cola.encolar(2)
mi_cola.encolar(4)
mi_cola.encolar(3)

# Mostrar la cola antes de eliminar repetidos
print("Antes de eliminar repetidos:")
mi_cola.mostrar_cola()

# Eliminar los elementos repetidos
mi_cola.eliminar_repetidos()

# Mostrar la cola después de eliminar repetidos
print("Después de eliminar repetidos:")
mi_cola.mostrar_cola()
