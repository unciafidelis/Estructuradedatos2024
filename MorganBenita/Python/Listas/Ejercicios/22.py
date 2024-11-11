class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleCircular:
    def __init__(self):
        # Nodo de cabecera, que siempre está presente y no contiene dato relevante.
        self.cabecera = Nodo(None)
        self.cabecera.siguiente = self.cabecera
        self.cabecera.anterior = self.cabecera

    # Método para insertar un nodo al inicio de la lista
    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        primero = self.cabecera.siguiente
        nuevo_nodo.siguiente = primero
        nuevo_nodo.anterior = self.cabecera
        self.cabecera.siguiente = nuevo_nodo
        primero.anterior = nuevo_nodo

    # Método para insertar un nodo al final de la lista
    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        ultimo = self.cabecera.anterior
        nuevo_nodo.siguiente = self.cabecera
        nuevo_nodo.anterior = ultimo
        ultimo.siguiente = nuevo_nodo
        self.cabecera.anterior = nuevo_nodo

    # Método para eliminar el primer nodo que contenga el dato especificado
    def eliminar(self, dato):
        actual = self.cabecera.siguiente
        while actual != self.cabecera:
            if actual.dato == dato:
                anterior = actual.anterior
                siguiente = actual.siguiente
                anterior.siguiente = siguiente
                siguiente.anterior = anterior
                return
            actual = actual.siguiente
        print(f"El elemento {dato} no se encontró en la lista.")

    # Método para buscar un elemento en la lista
    def buscar(self, dato):
        actual = self.cabecera.siguiente
        while actual != self.cabecera:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    # Método para recorrer la lista hacia adelante e imprimir los datos
    def recorrer_adelante(self):
        actual = self.cabecera.siguiente
        while actual != self.cabecera:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("Inicio")

    # Método para recorrer la lista hacia atrás e imprimir los datos
    def recorrer_atras(self):
        actual = self.cabecera.anterior
        while actual != self.cabecera:
            print(actual.dato, end=" -> ")
            actual = actual.anterior
        print("Inicio")

    # Método para insertar después de un nodo con valor específico
    def insertar_despues(self, dato, nuevo_dato):
        actual = self.cabecera.siguiente
        while actual != self.cabecera:
            if actual.dato == dato:
                nuevo_nodo = Nodo(nuevo_dato)
                siguiente = actual.siguiente
                nuevo_nodo.siguiente = siguiente
                nuevo_nodo.anterior = actual
                actual.siguiente = nuevo_nodo
                siguiente.anterior = nuevo_nodo
                return
            actual = actual.siguiente
        print(f"El nodo con el dato {dato} no se encontró en la lista.")

# Ejemplo de uso de la clase ListaDobleCircular
lista = ListaDobleCircular()
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
