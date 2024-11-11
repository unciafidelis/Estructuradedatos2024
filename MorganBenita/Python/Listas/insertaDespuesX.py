'''
'''
class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_antes_de(self, dato, x):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            return
        if self.cabeza.info == x:
            nuevo_nodo.liga = self.cabeza
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.liga and actual.liga.info != x:
            actual = actual.liga
        if actual.liga:
            nuevo_nodo.liga = actual.liga
            actual.liga = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.info, end=" -> ")
            actual = actual.liga
        print("None")

lista = ListaSimple()
lista.insertar_antes_de(10, 20)
lista.cabeza = Nodo(20)
lista.insertar_antes_de(10, 20)
lista.insertar_antes_de(5, 10)
lista.insertar_antes_de(15, 20)

print("Lista después de las inserciones:")
lista.mostrar_lista()
