'''
Este algoritmo inserta un nodo después de otro dado como referencia 
en una lista simplemente ligada. P es el apuntador al primer 
nodo de la lista, dato indica la información que se almacenará 
en el nuevo nodo y X representa el contenido -información- del 
nodo dado como referencia. q y t son variables de tipo apuntador. 
Info y liga son los campos de los nodos de la lista. Band es 
una variable de tipo entero. 
'''
class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_despues_de(self, dato, x):
        actual = self.cabeza
        while actual:
            if actual.info == x:
                nuevo_nodo = Nodo(dato)
                nuevo_nodo.liga = actual.liga
                actual.liga = nuevo_nodo
                return
            actual = actual.liga

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
lista.insertar_despues_de(15, 10)
lista.insertar_despues_de(25, 20)
lista.insertar_despues_de(35, 30)

print("Lista después de las inserciones:")
lista.mostrar_lista()
