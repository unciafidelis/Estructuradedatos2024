'''Este algoritmo inserta un nodo antes de otro dado como referencia con 
información x. P es el apuntador al primer nodo de la lista y dato es la 
información que se almacenará en el nuevo nodo Q, T y R son variables de tipo 
apuntador Infor, LigaDer y LigaIzq son los campos de cada nodo de la lista.'''

class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga_der = None
        self.liga_izq = None

class ListaDoble:
    def __init__(self):
        self.p = None

    def insertar_antes(self, dato, x):
        nuevo = Nodo(dato)
        if not self.p:  # Si la lista está vacía
            self.p = nuevo
            return
        actual = self.p
        while actual:
            if actual.info == x:
                if actual.liga_izq:  # Si no es el primer nodo
                    actual.liga_izq.liga_der = nuevo
                    nuevo.liga_izq = actual.liga_izq
                nuevo.liga_der = actual
                actual.liga_izq = nuevo
                if actual == self.p:  # Si es el primer nodo
                    self.p = nuevo
                return
            actual = actual.liga_der

    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.info, end=" <-> ")
            actual = actual.liga_der
        print("None")

# Ejemplo de uso
lista = ListaDoble()
lista.insertar_antes(10, None)  # Lista vacía, agregamos el primer nodo
lista.insertar_antes(20, 10)
lista.insertar_antes(30, 20)
lista.insertar_antes(25, 20)

print("Lista doblemente ligada después de insertar nodos:")
lista.mostrar_lista()
