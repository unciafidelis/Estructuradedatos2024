'''
Este algoritmo recorre una lista cuyo primer nodo esta apuntado por P.
Q es una variable de tipo apuntador. INFO y LIGA son los campos de
cada nodo de la lista.
'''
class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar(self, info):
        nuevo_nodo = Nodo(info)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.liga:
                actual = actual.liga
            actual.liga = nuevo_nodo

    def recorrer_lista(self):
        q = self.cabeza
        while q:
            print(q.info)
            q = q.liga

lista = ListaSimple()
lista.agregar(5)
lista.agregar(10)
lista.agregar(15)

print("Recorrido de la lista:")
lista.recorrer_lista()
