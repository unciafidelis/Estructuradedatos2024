'''Este algoritmo elimina el primer elemento de una lista doblemente ligada. 
P y F son los apuntadores al primer y último nodo de la lista respectivamente. 
Q es una variable de tipo apuntador. Infor, LigaDer y LigaIzq son los campos 
de cada nodo de la lista.'''

class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga_der = None
        self.liga_izq = None

class ListaDoble:
    def __init__(self):
        self.p = None
        self.f = None

    def eliminar_primer_elemento(self):
        if not self.p:  # Si la lista está vacía
            print("La lista está vacía")
            return
        if self.p == self.f:  # Si hay solo un nodo en la lista
            self.p = self.f = None
        else:
            self.p = self.p.liga_der  # Mover el primer nodo al siguiente
            self.p.liga_izq = None  # El nuevo primer nodo no tiene nodo anterior

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

lista.eliminar_primer_elemento()
print("Lista después de eliminar el primer elemento:")
lista.mostrar_lista()
