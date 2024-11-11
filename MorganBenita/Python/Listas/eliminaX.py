'''
Este algoritmo elimina un nodo con información X de una 
lista simplemente ligada. P es el apuntador al primer nodo 
de la lista. Q y T son variables de tipo apuntador Band 
es una variable de tipo entero info y liga son los campos 
de los nodos de la lista.
'''
class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def eliminar_x(self, x):
        p = self.cabeza
        # Si el primer nodo tiene la información que se quiere eliminar
        if p and p.info == x:
            self.cabeza = p.liga
            p = None
            return

        # Recorre la lista buscando el nodo con la información X
        while p and p.liga:
            if p.liga.info == x:
                t = p.liga
                p.liga = t.liga
                t = None
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

print("Lista original:")
lista.mostrar_lista()

lista.eliminar_x(20)

print("Lista después de eliminar el nodo con valor 20:")
lista.mostrar_lista()
