class Nodo:
    def __init__(self, dato):
        self.dato = dato           # Almacena el dato del nodo
        self.siguiente = None       # Apunta al siguiente nodo
        self.anterior = None        # Apunta al nodo anterior

class ListaDoble:
    def __init__(self):
        self.cabeza = None          # Primer nodo de la lista
        self.cola = None            # Último nodo de la lista

    # Método para insertar un nodo al inicio de la lista
    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:     # Si la lista está vacía
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    # Método para insertar un nodo al final de la lista
    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cola is None:       # Si la lista está vacía
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    # Método para eliminar un nodo con un valor específico
    def eliminar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:  # Si encontramos el dato a eliminar
                if actual == self.cabeza:  # Si el nodo es la cabeza
                    self.cabeza = actual.siguiente
                    if self.cabeza:
                        self.cabeza.anterior = None
                elif actual == self.cola:  # Si el nodo es la cola
                    self.cola = actual.anterior
                    self.cola.siguiente = None
                else:                      # Si está en medio
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                return
            actual = actual.siguiente
        print(f"El elemento {dato} no se encontró en la lista.")

    # Método para buscar un nodo con un valor específico
    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    # Método para recorrer e imprimir la lista de inicio a fin
    def recorrer_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Método para recorrer e imprimir la lista de fin a inicio
    def recorrer_atras(self):
        actual = self.cola
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.anterior
        print("None")

    # Método para insertar después de un nodo con un valor dado
    def insertar_despues(self, dato, nuevo_dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                nuevo_nodo = Nodo(nuevo_dato)
                nuevo_nodo.siguiente = actual.siguiente
                nuevo_nodo.anterior = actual
                if actual.siguiente:
                    actual.siguiente.anterior = nuevo_nodo
                else:  # Si actual es el último nodo, actualizar cola
                    self.cola = nuevo_nodo
                actual.siguiente = nuevo_nodo
                return
            actual = actual.siguiente
        print(f"El nodo con el dato {dato} no se encontró en la lista.")

# Ejemplo de uso de la clase ListaDoble
lista = ListaDoble()
lista.insertar_inicio(10)
lista.insertar_final(20)
lista.insertar_inicio(5)
lista.insertar_final(30)

print("Recorrido hacia adelante:")
lista.recorrer_adelante()

print("Recorrido hacia atrás:")
lista.recorrer_atras()

# Insertar después de un nodo específico
lista.insertar_despues(20, 25)
print("Después de insertar 25 después de 20:")
lista.recorrer_adelante()

# Eliminar un elemento específico
lista.eliminar(10)
print("Después de eliminar el nodo con dato 10:")
lista.recorrer_adelante()

# Buscar un elemento
print("Buscar 25 en la lista:", lista.buscar(25))
print("Buscar 40 en la lista:", lista.buscar(40))
