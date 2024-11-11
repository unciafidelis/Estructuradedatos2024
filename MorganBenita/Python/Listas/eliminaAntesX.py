'''
Este algoritmo permite eliminar el nodo anterior al nodo 
que contiene la información X en una lista simplemente ligada. 
P es el apuntador al primer nodo de la lista. 
Q, T y R son variables de tipo apuntador. 
Band es una variable de tipo entero info y liga son los campos 
de los nodos de la lista. 
'''
class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def eliminar_antes_x(self, x):
        # Si la lista está vacía o solo tiene un nodo
        if self.cabeza is None or self.cabeza.liga is None:
            return

        p = self.cabeza
        # Si el primer nodo contiene la información x
        if p.liga and p.liga.info == x:
            self.cabeza = p.liga
            p = None
            return
        
        # Recorre la lista buscando el nodo antes del nodo que contiene la información X
        while p.liga and p.liga.liga:
            if p.liga.liga.info == x:
                t = p
                p = p.liga
                t.liga = p.liga
                p = None
                return
            p = p.liga

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.info, end=" -> ")
            actual = actual.liga
        print("None")

lista = ListaSimple()
lista.cabeza = Nodo(10)
lista.cabeza.liga = Nodo(20)
lista.cabeza.liga.liga = Nodo(30)
lista.cabeza.liga.liga.liga = Nodo(40)

print("Lista original:")
lista.mostrar_lista()

lista.eliminar_antes_x(30)

print("Lista después de eliminar el nodo antes de 30:")
lista.mostrar_lista()
