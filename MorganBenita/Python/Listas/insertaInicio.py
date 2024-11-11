'''
Este algoritmo inserta un nodo al inicio 
de una lista simplemente ligada. P es el
apuntador al primer nodo de la misma, DATO es
la información que se almacenará en el 
nuevo nodo.
Q es una variable de tipo apuntador. INFO y LIGA 
son los campos de cada nodo de la lista.
'''
class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def inserta_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.liga = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.info)
            actual = actual.liga

lista = ListaSimple()
lista.inserta_inicio(5)
lista.inserta_inicio(10)
lista.inserta_inicio(15)

print("Lista después de inserciones al inicio:")
lista.mostrar_lista()
