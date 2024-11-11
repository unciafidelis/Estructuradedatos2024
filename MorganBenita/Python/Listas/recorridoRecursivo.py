'''
Este algoritmo recorre una lista simplemente ligada de forma
recursiva. P es un apuntador al nodo que se va a visitar. La 
primera vez trae la dirección del primer nodo de la lista.
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

    def recorre_recursivo(self, p):
        if p:
            print(p.info)
            self.recorre_recursivo(p.liga)

lista = ListaSimple()
lista.agregar(5)
lista.agregar(10)
lista.agregar(15)

print("Recorrido recursivo de la lista:")
lista.recorre_recursivo(lista.cabeza)
