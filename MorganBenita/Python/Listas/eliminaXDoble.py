'''Este algoritmo elimina el nodo con información x de una lista doblemente ligada. 
P y F son los apuntadores al primero y último nodo de la lista respectivamente. 
Q, T y R son variables de tipo apuntador. Infor, LigaDer y LigaIzq son los campos de cada nodo de la lista.'''

class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga_der = None
        self.liga_izq = None

class ListaDoble:
    def __init__(self):
        self.p = None
        self.f = None

    def eliminar_elemento(self, x):
        if not self.p:  # Si la lista está vacía
            print("La lista está vacía")
            return
        actual = self.p
        while actual:  # Recorrer la lista
            if actual.info == x:  # Si encontramos el nodo con el valor x
                if actual == self.p:  # Si es el primer nodo
                    self.p = actual.liga_der
                    if self.p:  # Si hay más nodos, actualizar el liga_izq del siguiente nodo
                        self.p.liga_izq = None
                elif actual == self.f:  # Si es el último nodo
                    self.f = actual.liga_izq
                    if self.f:  # Si hay más nodos, actualizar el liga_der del anterior nodo
                        self.f.liga_der = None
                else:  # Si es un nodo intermedio
                    actual.liga_izq.liga_der = actual.liga_der
                    if actual.liga_der:  # Si hay nodo siguiente, actualizar el liga_izq
                        actual.liga_der.liga_izq = actual.liga_izq
                print(f"Elemento {x} eliminado.")
                return
            actual = actual.liga_der
        print(f"Elemento {x} no encontrado.")

    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.info, end=" <-> ")
            actual = actual.liga_der
        print("None")

# Ejemplo de uso
lista = ListaDoble()
lista.p = Nodo(10)
lista.f = lista.p
lista.p.liga_der = Nodo(20)
lista.p.liga_der.liga_izq = lista.p
lista.f = lista.p.liga_der
lista.p.liga_der.liga_der = Nodo(30)
lista.p.liga_der.liga_der.liga_izq = lista.p.liga_der
lista.f = lista.p.liga_der.liga_der

print("Lista original:")
lista.mostrar_lista()

lista.eliminar_elemento(20)
print("Lista después de eliminar el elemento 20:")
lista.mostrar_lista()

lista.eliminar_elemento(40)  # Intentar eliminar un elemento no existente
