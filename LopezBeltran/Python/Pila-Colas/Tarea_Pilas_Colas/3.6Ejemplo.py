# Ejemplo 3.6 
class ColaCircular:
    MAX = 7

    def __init__(self):
        self.cola = [None] * self.MAX
        self.frente = 0
        self.final = 0
        self.size = 0

    def es_vacia(self):
        return self.size == 0

    def es_llena(self):
        return self.size == self.MAX

    def insertar(self, elemento):
        if self.es_llena():
            raise OverflowError("Error: Cola llena (desbordamiento).")
        self.cola[self.final] = elemento
        self.final = (self.final + 1) % self.MAX
        self.size += 1

    def eliminar(self):
        if self.es_vacia():
            raise IndexError("Error: Cola vacía (no hay elementos para eliminar).")
        elemento = self.cola[self.frente]
        self.cola[self.frente] = None  # Opcional: limpiar el valor
        self.frente = (self.frente + 1) % self.MAX
        self.size -= 1
        return elemento

    def mostrar(self):
        if self.es_vacia():
            return "Cola vacía."
        return [self.cola[(self.frente + i) % self.MAX] for i in range(self.size)]

# Ejemplo de uso
cola = ColaCircular()

# Insertar elementos
cola.insertar("Lunes")
cola.insertar("Martes")
cola.insertar("Miércoles")
cola.insertar("Jueves")
cola.insertar("Viernes")

# Mostrar estado de la cola
print("Estado inicial de la cola: ", cola.mostrar())

# Eliminar Lunes
cola.eliminar()
print("Estado después de eliminar Lunes: ", cola.mostrar())

# Insertar Sábado
cola.insertar("Sábado")
print("Estado después de insertar Sábado: ", cola.mostrar())

# Eliminar Martes, Miércoles, Jueves y Viernes
cola.eliminar()  # Martes
cola.eliminar()  # Miércoles
cola.eliminar()  # Jueves
cola.eliminar()  # Viernes
print("Estado después de eliminar Martes, Miércoles, Jueves y Viernes: ", cola.mostrar())

# Insertar Domingo
cola.insertar("Domingo")
print("Estado después de insertar Domingo: ", cola.mostrar())

# Eliminar Sábado
cola.eliminar()  # Sábado
print("Estado después de eliminar Sábado: ", cola.mostrar())

# Estado final de la cola
print("Estado final de la cola: ", cola.mostrar())
