class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Almacena el dato del nodo
        self.siguiente = None  # Apunta al siguiente nodo, inicialmente es None

class ListaSimplementeLigada:
    def __init__(self):
        self.cabeza = None  # La lista comienza vacía (sin nodos)

    # Método para insertar un elemento al final de la lista
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo  # Si la lista está vacía, el nuevo nodo será la cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:  # Recorre la lista hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # Inserta el nuevo nodo al final

    # Método para eliminar un elemento de la lista
    def eliminar(self, dato):
        if not self.cabeza:  # Si la lista está vacía
            print("La lista está vacía.")
            return

        # Si el elemento a eliminar es la cabeza
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return

        # Si el elemento a eliminar no es la cabeza, se busca en el resto de la lista
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == dato:  # Si encontramos el nodo con el dato
                actual.siguiente = actual.siguiente.siguiente  # Se elimina el nodo
                return
            actual = actual.siguiente
        print("El dato no se encuentra en la lista.")

    # Método para recorrer la lista e imprimir sus elementos
    def recorrer(self):
        if not self.cabeza:
            print("La lista está vacía.")
            return
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")  # Al final de la lista se imprime "None"

    # Método para eliminar elementos repetidos de la lista
    def eliminar_repetidos(self):
        if not self.cabeza:
            return

        elementos_vistos = set()  # Usamos un set para hacer seguimiento de los elementos visitados
        actual = self.cabeza
        prev = None

        while actual:
            if actual.dato in elementos_vistos:
                # Eliminar el nodo actual (repetido)
                prev.siguiente = actual.siguiente
            else:
                # Si no es repetido, lo agregamos al set de elementos vistos
                elementos_vistos.add(actual.dato)
                prev = actual
            actual = actual.siguiente

# Ejemplo de uso
lista = ListaSimplementeLigada()

# Insertamos elementos
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.insertar(20)  # Elemento repetido
lista.insertar(40)

# Mostrar la lista
print("Lista antes de eliminar repetidos:")
lista.recorrer()

# Eliminar elementos repetidos
lista.eliminar_repetidos()

# Mostrar la lista después de eliminar los repetidos
print("Lista después de eliminar repetidos:")
lista.recorrer()

# Eliminar un elemento
lista.eliminar(30)
print("Lista después de eliminar el elemento 30:")
lista.recorrer()
