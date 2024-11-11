class Nodo:
    def __init__(self, info):
        self.info = info  # Información del nodo
        self.liga_der = None  # Puntero al siguiente nodo

class Pila:
    def __init__(self):
        self.top = None  # La pila comienza vacía, sin elementos

    # Subprograma para insertar un elemento en la pila
    def mete_pila(self, elemento):
        nuevo_nodo = Nodo(elemento)  # Creamos un nuevo nodo con el valor dado
        nuevo_nodo.liga_der = self.top  # Hacemos que el siguiente del nuevo nodo apunte al nodo superior actual
        self.top = nuevo_nodo  # El nuevo nodo es ahora el nodo superior de la pila

    # Subprograma para eliminar un elemento de la pila
    def saca_pila(self):
        if not self.esta_vacia():  # Verificamos si la pila no está vacía
            elemento = self.top.info  # Obtenemos el valor del nodo superior
            self.top = self.top.liga_der  # Movemos el puntero al siguiente nodo
            return elemento  # Devolvemos el valor eliminado
        else:
            print("Pila vacía. No se puede sacar elemento.")
            return None

    # Verifica si la pila está vacía
    def esta_vacia(self):
        return self.top is None

    # Método para mostrar el contenido de la pila
    def mostrar_pila(self):
        if self.esta_vacia():
            print("La pila está vacía.")
        else:
            actual = self.top
            print("Contenido de la pila:", end=" ")
            while actual:
                print(actual.info, end=" -> ")
                actual = actual.liga_der
            print("None")

# Ejemplo de uso
pila = Pila()

# Insertamos elementos en la pila
pila.mete_pila(10)
pila.mete_pila(20)
pila.mete_pila(30)

# Mostramos la pila
pila.mostrar_pila()

# Sacamos un elemento de la pila
elemento = pila.saca_pila()
print("Elemento sacado de la pila:", elemento)

# Mostramos la pila después de sacar un elemento
pila.mostrar_pila()

# Sacamos otro elemento
elemento = pila.saca_pila()
print("Elemento sacado de la pila:", elemento)

# Mostramos la pila después de sacar el segundo elemento
pila.mostrar_pila()
