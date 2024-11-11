class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga_der = None  # Puntero al siguiente nodo
        self.liga_izq = None  # Puntero al nodo anterior

class ListaDoble:
    def __init__(self):
        self.p = None  # Primer nodo de la lista

    # Insertar un nodo al final de la lista doblemente ligada
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.p:
            self.p = nuevo_nodo  # El primer nodo es el nuevo nodo
        else:
            actual = self.p
            while actual.liga_der:  # Recorre hasta el final de la lista
                actual = actual.liga_der
            actual.liga_der = nuevo_nodo
            nuevo_nodo.liga_izq = actual

    # Función recursiva para insertar un elemento después de un nodo dado
    def insertar_despues(self, nodo_ref, dato):
        # Caso base: Si el nodo de referencia es None, no se puede insertar
        if not nodo_ref:
            print("Nodo de referencia no encontrado.")
            return
        
        nuevo_nodo = Nodo(dato)

        # Insertamos el nuevo nodo después del nodo de referencia
        nuevo_nodo.liga_der = nodo_ref.liga_der  # El siguiente nodo de referencia pasa a ser el siguiente del nuevo nodo
        nuevo_nodo.liga_izq = nodo_ref  # El anterior del nuevo nodo es el nodo de referencia

        # Actualizamos el nodo de referencia (si existe un siguiente nodo)
        if nodo_ref.liga_der:
            nodo_ref.liga_der.liga_izq = nuevo_nodo  # Si hay un nodo después, su liga_izq apunta al nuevo nodo

        nodo_ref.liga_der = nuevo_nodo  # El nodo de referencia apunta al nuevo nodo

    # Mostrar lista desde el inicio hasta el final
    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.info, end=" <-> ")
            actual = actual.liga_der
        print("None")

# Ejemplo de uso
lista = ListaDoble()

# Insertamos algunos elementos en la lista
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)

print("Lista original:")
lista.mostrar_lista()

# Referencia a un nodo específico (por ejemplo, el nodo con valor 20)
nodo_ref = lista.p.liga_der  # Nodo que contiene el valor 20

# Insertamos un nuevo elemento después del nodo con valor 20
lista.insertar_despues(nodo_ref, 25)

print("Lista después de insertar 25 después del nodo con valor 20:")
lista.mostrar_lista()
