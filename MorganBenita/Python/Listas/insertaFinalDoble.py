'''Este algoritmo inserta un nodo al final de una lista doblemente ligada. 
F es el apuntador al último nodo de la lista y dato es la información 
que se almacenará en el nuevo nodo. Q es una variable de tipo puntero. 
Infor, ligaizq y ligader son los campos de cada nodo de la lista.'''

class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga_der = None
        self.liga_izq = None

class ListaDoble:
    def __init__(self):
        self.p = None

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if not self.p:
            self.p = nuevo
        else:
            f = self.p
            while f.liga_der:
                f = f.liga_der
            f.liga_der = nuevo
            nuevo.liga_izq = f

    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.info, end=" <-> ")
            actual = actual.liga_der
        print("None")

# Ejemplo de uso
lista = ListaDoble()
lista.insertar_final(10)
lista.insertar_final(20)
lista.insertar_final(30)
lista.insertar_final(40)

print("Lista doblemente ligada:")
lista.mostrar_lista()
