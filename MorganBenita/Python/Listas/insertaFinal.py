'''
Este algoritmo inserta un nodo al final de una lista 
simplemente ligada. P es el apuntador al primer nodo 
de la lista y dato es el es la información que se 
almacenará en el nuevo nodo. Q y T son variables de 
tipo puntero. Info y liga son los campos de cada nodo de la lista.
'''
class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def inserta_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.liga:
                actual = actual.liga
            actual.liga = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.info)
            actual = actual.liga

lista = ListaSimple()
lista.inserta_final(5)
lista.inserta_final(10)
lista.inserta_final(15)

print("Lista después de inserciones al final:")
lista.mostrar_lista()

