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

    def mostrar(self):
        if not self.es_vacia():
            return self.items[self.frente - 1:self.final]
        return []

# Ejemplo de uso
max_elementos = 5
cola = Cola(max_elementos)

# Insertar elementos
cola.insertar(10)
cola.insertar(20)
cola.insertar(30)

# Mostrar la cola
print("Elementos en la cola:", cola.mostrar())

# Intentar insertar más elementos
cola.insertar(40)
cola.insertar(50)
cola.insertar(60)  # Esto debería mostrar un mensaje de desbordamiento

# Mostrar la cola después de las inserciones
print("Elementos en la cola después de insertar:", cola.mostrar())
