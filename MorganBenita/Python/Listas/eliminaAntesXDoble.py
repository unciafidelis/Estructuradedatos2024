'''Este algoritmo elimina si se puede el nodo anterior a aquel que contiene la 
información x. P es el apuntador al primer nodo de la lista. Q, T y R son 
variables de tipo apuntador. Infor, LigaDer y LigaIzq son los campos de cada 
nodo de la lista.'''

class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga_der = None
        self.liga_izq = None

class ListaDoble:
    def __init__(self):
        self.p = None
        self.f = None

    def eliminar_anterior_a_x(self, x):
        if not self.p:  # Si la lista está vacía
            print("La lista está vacía")
            return
        actual = self.p
        while actual and actual.liga_der:  # Aseguramos que hay un nodo siguiente
            if actual.liga_der.info == x:  # Si el siguiente nodo tiene la info x
                nodo_anterior = actual
                if nodo_anterior == self.p:  # Si el nodo anterior es el primero
                    self.p = nodo_anterior.liga_der
                    self.p.liga_izq = None
                else:  # Si el nodo anterior no es el primero
                    nodo_anterior.liga_izq.liga_der = nodo_anterior.liga_der
                    nodo_anterior.liga_der.liga_izq = nodo_anterior.liga_izq
                print(f"Nodo anterior al nodo con información {x} eliminado.")
                return
            actual = actual.liga_der
        print(f"No se encontró un nodo anterior al nodo con información {x}.")

    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.info, end=" <-> ")
            actual = actual.liga_der
        print("None")

# Ejemplo de uso
lista = ListaDoble()
lista.p = Nodo(10)
lista.f = lista.p
lista.p.liga_der = Nodo(20)
lista.p.liga_der.liga_izq = lista.p
lista.f = lista.p.liga_der
lista.p.liga_der.liga_der = Nodo(30)
lista.p.liga_der.liga_der.liga_izq = lista.p.liga_der
lista.f = lista.p.liga_der.liga_der

print("Lista original:")
lista.mostrar_lista()

lista.eliminar_anterior_a_x(30)
print("Lista después de eliminar el nodo anterior al 30:")
lista.mostrar_lista()

lista.eliminar_anterior_a_x(10)  # Intentar eliminar el nodo anterior al primer nodo
