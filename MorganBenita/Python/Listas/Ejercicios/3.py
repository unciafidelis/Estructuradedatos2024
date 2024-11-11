'''Este algoritmo inserta un elemento en una lista ordenada, de tal manera 
que no se altere el orden de la misma. P es el apuntador al primer nodo 
de la lista y dato es la información que se almacenará en el nuevo nodo. 
Q y T son variables de tipo apuntador. Infor, LigaDer y LigaIzq son los 
campos de cada nodo de la lista.'''

class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga_der = None
        self.liga_izq = None

class ListaDoble:
    def __init__(self):
        self.p = None
        self.f = None

    def insertar_ordenado(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.p:  # Si la lista está vacía
            self.p = self.f = nuevo_nodo
            return
        actual = self.p
        # Insertar en el inicio
        if dato < self.p.info:
            nuevo_nodo.liga_der = self.p
            self.p.liga_izq = nuevo_nodo
            self.p = nuevo_nodo
            return
        # Buscar la posición correcta en la lista
        while actual and actual.info < dato:  # Recorremos la lista hasta encontrar el lugar adecuado
            actual = actual.liga_der
        
        if actual:  # Si encontramos el lugar donde insertar
            nuevo_nodo.liga_izq = actual.liga_izq
            nuevo_nodo.liga_der = actual
            if actual.liga_izq:
                actual.liga_izq.liga_der = nuevo_nodo
            actual.liga_izq = nuevo_nodo
        else:  # Si el valor debe ir al final
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
lista.insertar_ordenado(10)
lista.insertar_ordenado(30)
lista.insertar_ordenado(20)
lista.insertar_ordenado(25)

print("Lista ordenada después de las inserciones:")
lista.mostrar_lista()

