class Nodo:
    def __init__(self, info):
        self.info = info
        self.siguiente = None  # Puntero al siguiente nodo

class ListaCircular:
    def __init__(self):
        self.p = None  # Puntero al primer nodo de la lista

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.p:  # Si la lista está vacía, el nuevo nodo es el único
            self.p = nuevo_nodo
            nuevo_nodo.siguiente = self.p  # El nodo apunta a sí mismo
        else:
            actual = self.p
            # Recorremos la lista hasta llegar al último nodo
            while actual.siguiente != self.p:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # El último nodo apunta al nuevo nodo
            nuevo_nodo.siguiente = self.p  # El nuevo nodo apunta al primer nodo

    def mostrar_lista(self):
        if not self.p:
            print("Lista vacía.")
            return
        actual = self.p
        while True:
            print(actual.info, end=" -> ")
            actual = actual.siguiente
            if actual == self.p:
                break
        print("(circular)")

    def eliminar(self, x):
        if not self.p:  # Si la lista está vacía, no hay nada que eliminar
            print("Lista vacía. No se puede eliminar.")
            return

        actual = self.p
        anterior = None

        # Caso especial: si el nodo a eliminar es el primero de la lista
        if self.p.info == x:
            if actual.siguiente == self.p:  # Solo hay un nodo en la lista
                self.p = None
            else:
                # Recorremos hasta el último nodo
                while actual.siguiente != self.p:
                    actual = actual.siguiente
                # Ajustamos los punteros para eliminar el primer nodo
                actual.siguiente = self.p.siguiente
                self.p = self.p.siguiente
            return

        # Buscamos el nodo que contiene el valor x
        while actual != self.p and actual.info != x:
            anterior = actual
            actual = actual.siguiente

        if actual.info == x:  # Si encontramos el nodo con el valor x
            anterior.siguiente = actual.siguiente  # El nodo anterior apunta al siguiente del nodo actual
        else:
            print(f"El valor {x} no se encuentra en la lista.")

# Ejemplo de uso
lista = ListaCircular()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.insertar(40)

print("Lista original:")
lista.mostrar_lista()

# Eliminar un elemento
lista.eliminar(30)
print("\nLista después de eliminar 30:")
lista.mostrar_lista()

# Eliminar el primer elemento
lista.eliminar(10)
print("\nLista después de eliminar 10:")
lista.mostrar_lista()

# Eliminar un elemento no presente
lista.eliminar(50)
