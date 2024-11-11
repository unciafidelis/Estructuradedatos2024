class Nodo:
    def __init__(self, info):
        self.info = info
        self.siguiente = None  # Puntero al siguiente nodo

class ListaCircular:
    def __init__(self):
        self.p = None  # Puntero al primer nodo de la lista

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.p:  # Si la lista está vacía
            self.p = nuevo_nodo
            nuevo_nodo.siguiente = self.p  # El nodo apunta a sí mismo, formando la circularidad
        else:
            actual = self.p
            # Recorremos la lista hasta llegar al último nodo
            while actual.siguiente != self.p:
                actual = actual.siguiente
            # El último nodo apunta al nuevo nodo
            actual.siguiente = nuevo_nodo
            # El nuevo nodo apunta al primer nodo
            nuevo_nodo.siguiente = self.p

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

# Ejemplo de uso
lista = ListaCircular()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.insertar(40)

print("Lista circular:")
lista.mostrar_lista()
