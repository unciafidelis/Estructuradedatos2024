class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga_der = None

class Lista:
    def __init__(self):
        self.p = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.p:
            self.p = nuevo_nodo
        else:
            actual = self.p
            while actual.liga_der:
                actual = actual.liga_der
            actual.liga_der = nuevo_nodo

    def mostrar_lista_recursiva(self, nodo):
        # Caso base: Si el nodo es None, terminamos la recursión
        if not nodo:
            return
        # Imprimir el valor del nodo actual
        print(nodo.info, end=" -> ")
        # Llamada recursiva al siguiente nodo
        self.mostrar_lista_recursiva(nodo.liga_der)

# Ejemplo de uso
lista = Lista()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.insertar(40)

print("Lista completa (recursiva):")
lista.mostrar_lista_recursiva(lista.p)
print("None")
