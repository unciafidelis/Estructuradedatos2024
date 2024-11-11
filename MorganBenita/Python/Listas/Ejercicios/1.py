'''Este algoritmo inserta, si es posible, un elemento antes de otro nodo dado como 
referencia en una lista ordenada. P es el apuntador al primer nodo de la lista, 
dato es la información que se almacenará en el nuevo nodo y x representa la 
información del nodo dado como referencia. Q, T y R son variables de tipo 
apuntador. Infor, LigaDer y LigaIzq son los campos de cada nodo de la lista.'''

class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga_der = None
        self.liga_izq = None

class ListaDoble:
    def __init__(self):
        self.p = None
        self.f = None

    def insertar_antes_ordenado(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.p:  # Si la lista está vacía
            self.p = self.f = nuevo_nodo
            return
        actual = self.p
        while actual and actual.info < dato:  # Recorremos hasta encontrar el lugar correcto
            actual = actual.liga_der
        
        if actual:  # Si encontramos el nodo con el valor adecuado
            if actual == self.p:  # Si el nodo a insertar es el primero
                nuevo_nodo.liga_der = self.p
                self.p.liga_izq = nuevo_nodo
                self.p = nuevo_nodo
            else:  # Si el nodo a insertar no es el primero
                nuevo_nodo.liga_izq = actual.liga_izq
                nuevo_nodo.liga_der = actual
                if actual.liga_izq:
                    actual.liga_izq.liga_der = nuevo_nodo
                actual.liga_izq = nuevo_nodo
        else:  # Si el valor es mayor que todos los existentes
            self.f.liga_der = nuevo_nodo
            nuevo_nodo.liga_izq = self.f
            self.f = nuevo_nodo

    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.info, end=" <-> ")
            actual = actual.liga_der
        print("None")

# Ejemplo de uso
lista = ListaDoble()
lista.insertar_antes_ordenado(10)
lista.insertar_antes_ordenado(30)
lista.insertar_antes_ordenado(20)
lista.insertar_antes_ordenado(25)

print("Lista ordenada después de las inserciones:")
lista.mostrar_lista()
