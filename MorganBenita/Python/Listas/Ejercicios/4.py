'''Este algoritmo elimina un nodo de una lista ordenada. P es el apuntador al primer 
nodo de la lista y dato es la información del nodo que se desea eliminar. 
Q y T son variables de tipo apuntador. Infor, LigaDer y LigaIzq son los 
campos de cada nodo de la lista.'''

class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga_der = None
        self.liga_izq = None

class ListaDoble:
    def __init__(self):
        self.p = None
        self.f = None

    def insertar_ordenado(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.p:  # Si la lista está vacía
            self.p = self.f = nuevo_nodo
        elif dato <= self.p.info:  # Insertar al inicio
            nuevo_nodo.liga_der = self.p
            self.p.liga_izq = nuevo_nodo
            self.p = nuevo_nodo
        else:
            actual = self.p
            while actual.liga_der and actual.liga_der.info < dato:
                actual = actual.liga_der
            nuevo_nodo.liga_der = actual.liga_der
            if actual.liga_der:
                actual.liga_der.liga_izq = nuevo_nodo
            nuevo_nodo.liga_izq = actual
            if actual == self.f:  # Si es el último nodo
                self.f = nuevo_nodo
            actual.liga_der = nuevo_nodo

    def eliminar_ordenado(self, dato):
        if not self.p:  # Si la lista está vacía
            print("La lista está vacía.")
            return
        actual = self.p
        
        # Si el nodo a eliminar es el primero
        if self.p.info == dato:
            if self.p == self.f:  # Si solo hay un nodo
                self.p = self.f = None
            else:
                self.p = self.p.liga_der
                self.p.liga_izq = None
            return
        
        # Buscar el nodo que contiene la información dada
        while actual and actual.info != dato:
            actual = actual.liga_der
        
        if actual:  # Si encontramos el nodo
            if actual == self.f:  # Si el nodo a eliminar es el último
                self.f = actual.liga_izq
                self.f.liga_der = None
            else:  # Si el nodo está en el medio
                actual.liga_izq.liga_der = actual.liga_der
                actual.liga_der.liga_izq = actual.liga_izq
        else:
            print(f"El nodo con valor {dato} no se encuentra en la lista.")

    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.info, end=" <-> ")
            actual = actual.liga_der
        print("None")

# Ejemplo de uso
lista = ListaDoble()
lista.insertar_ordenado(10)
lista.insertar_ordenado(30)
lista.insertar_ordenado(20)
lista.insertar_ordenado(25)

print("Lista ordenada antes de eliminar:")
lista.mostrar_lista()

# Eliminar el nodo con valor 20
lista.eliminar_ordenado(20)

print("Lista después de eliminar el nodo con valor 20:")
lista.mostrar_lista()

# Intentar eliminar un nodo que no existe
lista.eliminar_ordenado(50)
