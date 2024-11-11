'''
Este algoritmo permite eliminar el primer elemento de una lista 
simplemente ligada. P es el apuntador al primer nodo de la lista. 
Q es una variable de tipo apuntador. Info y liga son los campos 
de los nodos de la lista. 
'''
class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def eliminar_inicio(self):
        if self.cabeza:
            self.cabeza = self.cabeza.liga

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

lista.eliminar_inicio()

print("Lista después de eliminar el primer nodo:")
lista.mostrar_lista()
