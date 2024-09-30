class Cola:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = []
        self.frente = 0  # Índice del frente de la cola
        self.final = 0    # Índice del final de la cola

    def es_llena(self):
        return self.final >= self.max_size

    def es_vacia(self):
        return self.frente == self.final

    def insertar(self, dato):
        if not self.es_llena():
            self.items.append(dato)  # Agregar el dato al final de la cola
            self.final += 1  # Actualizar el índice del final
            if self.final == 1:  # Si es el primer elemento
                self.frente = 1  # Actualizar el frente
        else:
            print("Desbordamiento - Cola llena")

    def eliminar(self):
        if not self.es_vacia():  # Verifica que la cola no esté vacía
            dato = self.items[self.frente - 1]  # Obtener el primer elemento
            if self.frente == self.final:  # Si hay un solo elemento
                self.frente = 0  # Indica cola vacía
                self.final = 0
            else:
                self.frente += 1  # Actualizar el índice del frente
            return dato
        else:
            print("Subdesbordamiento - Cola vacía")
            return None

# Ejemplo de uso
max_elementos = 5
cola = Cola(max_elementos)

# Insertar elementos
cola.insertar(10)
cola.insertar(20)
cola.insertar(30)

# Eliminar un elemento
elemento_eliminado = cola.eliminar()
print(f"Elemento eliminado: {elemento_eliminado}")

# Mostrar estado de la cola después de la eliminación
print("Estado de la cola:", cola.items[cola.fronte - 1:cola.rear])

# Intentar eliminar más elementos
cola.eliminar()
cola.eliminar()
cola.eliminar()  # Esto debería mostrar un mensaje de subdesbordamiento
