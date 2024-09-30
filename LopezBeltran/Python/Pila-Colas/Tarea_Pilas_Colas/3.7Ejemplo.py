# Ejemplo 3.7
class ColaCircular:
    MAX = 8

    def __init__(self):
        self.cola = [None] * self.MAX
        self.fronte = 0
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
        elemento = self.cola[self.fronte]
        self.cola[self.fronte] = None  # Opcional: limpiar el valor
        self.fronte = (self.fronte + 1) % self.MAX
        self.size -= 1
        return elemento

    def mostrar(self):
        if self.es_vacia():
            return "Cola vacía."
        return [self.cola[(self.fronte + i) % self.MAX] for i in range(self.size)]

# Ejemplo de uso
cola = ColaCircular()

# Insertar elementos
cola.insertar("XX")
cola.insertar("YY")
cola.insertar("ZZ")
cola.insertar("KK")
cola.insertar("TT")
cola.insertar("VV")
cola.insertar("NN")

# Mostrar estado de la cola
print("Estado de la cola después de insertar: ", cola.mostrar())

# Eliminar elementos en el orden XX, YY, ZZ, KK, TT, VV
for _ in range(6):
    cola.eliminar()

# Mostrar estado de la cola
print("Estado de la cola después de eliminar algunos elementos: ", cola.mostrar())

# Eliminar el siguiente elemento RR
try:
    cola.insertar("RR")  # Insertar para mostrar el estado
    cola.eliminar()  # Eliminar RR
except OverflowError as e:
    print(e)

# Mostrar estado de la cola
print("Estado de la cola tras eliminar RR: ", cola.mostrar())

# Eliminar NN
cola.eliminar()

# Mostrar estado final de la cola
print("Estado final de la cola: ", cola.mostrar())
