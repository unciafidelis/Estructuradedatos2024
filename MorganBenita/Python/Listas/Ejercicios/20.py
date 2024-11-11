class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Almacena el dato del nodo
        self.siguiente = None  # Apunta al siguiente nodo, inicialmente es None

class ListaCircularConCabecera:
    def __init__(self):
        self.cabecera = Nodo(None)  # Nodo de cabecera que no almacena datos
        self.cabecera.siguiente = self.cabecera  # El nodo de cabecera apunta a sí mismo

    # Método para insertar un elemento al final de la lista
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        actual = self.cabecera

        # Recorremos hasta encontrar el último nodo (aquel cuyo siguiente apunta a la cabecera)
        while actual.siguiente != self.cabecera:
            actual = actual.siguiente
        
        # Insertamos el nuevo nodo al final
        actual.siguiente = nuevo_nodo
        nuevo_nodo.siguiente = self.cabecera  # El último nodo apunta a la cabecera

    # Método para eliminar un elemento de la lista
    def eliminar(self, dato):
        if self.cabecera.siguiente == self.cabecera:  # Si la lista está vacía
            print("La lista está vacía.")
            return

        actual = self.cabecera
        while actual.siguiente != self.cabecera:
            if actual.siguiente.dato == dato:  # Si encontramos el nodo con el dato
                actual.siguiente = actual.siguiente.siguiente  # Elimina el nodo
                return
            actual = actual.siguiente
        
        print("El dato no se encuentra en la lista.")

    # Método para recorrer la lista e imprimir sus elementos
    def recorrer(self):
        if self.cabecera.siguiente == self.cabecera:  # Si la lista está vacía
            print("La lista está vacía.")
            return
        
        actual = self.cabecera.siguiente
        while actual != self.cabecera:  # Recorremos hasta que lleguemos nuevamente a la cabecera
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("Volver a la cabecera")  # Indica que hemos completado el ciclo

    # Método para eliminar elementos repetidos de la lista
    def eliminar_repetidos(self):
        if self.cabecera.siguiente == self.cabecera:  # Si la lista está vacía
            return

        elementos_vistos = set()  # Usamos un set para hacer seguimiento de los elementos visitados
        actual = self.cabecera.siguiente
        anterior = self.cabecera

        while actual != self.cabecera:
            if actual.dato in elementos_vistos:
                # Eliminar el nodo actual (repetido)
                anterior.siguiente = actual.siguiente
            else:
                # Si no es repetido, lo agregamos al set de elementos vistos
                elementos_vistos.add(actual.dato)
                anterior = actual
            actual = actual.siguiente

# Ejemplo de uso
lista = ListaCircularConCabecera()

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
