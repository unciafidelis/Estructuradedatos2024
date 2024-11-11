'''
Este algoritmo permite buscar el elemento con información X 
en una lista simplemente ligada que se encuentra desordenada. 
P es el apuntador al primer nodo de la lista. Q es una variable 
de tipo apuntador. Info y Liga son campos de los nodos de la lista.
'''
class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def buscar_desordenada(self, x):
        p = self.cabeza
        while p:
            if p.info == x:
                return True 
            p = p.liga
        return False 

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.info, end=" -> ")
            actual = actual.liga
        print("None")

lista = ListaSimple()
lista.cabeza = Nodo(10)
lista.cabeza.liga = Nodo(30)
lista.cabeza.liga.liga = Nodo(20)
lista.cabeza.liga.liga.liga = Nodo(40)

print("Lista original:")
lista.mostrar_lista()

resultado = lista.buscar_desordenada(30)
print("¿El 30 está en la lista?", resultado)

resultado = lista.buscar_desordenada(50)
print("¿El 50 está en la lista?", resultado)
