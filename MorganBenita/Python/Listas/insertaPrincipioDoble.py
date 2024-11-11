'''Este algoritmo inserta un nodo al inicio de una lista doblemente ligada. 
P es el apuntador al primer nodo de la lista y dato es la información 
que se almacenará en el nuevo nodo. Q es una variable de tipo apuntador 
Infor, LigaDer y LigaIzq son los campos de cada nodo de la lista.'''

class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga_der = None
        self.liga_izq = None

class ListaDoble:
    def __init__(self):
        self.p = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if not self.p:
            self.p = nuevo
        else:
            nuevo.liga_der = self.p
            self.p.liga_izq = nuevo
            self.p = nuevo

    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.info, end=" <-> ")
            actual = actual.liga_der
        print("None")

# Ejemplo de uso
lista = ListaDoble()
lista.insertar_inicio(10)
lista.insertar_inicio(20)
lista.insertar_inicio(30)
lista.insertar_inicio(40)

print("Lista doblemente ligada:")
lista.mostrar_lista()
