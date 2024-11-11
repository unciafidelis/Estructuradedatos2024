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

    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.info, end=" -> ")
            actual = actual.liga_der
        print("None")

    def dividir_lista(self, nodo, positivos, negativos):
        # Caso base: si el nodo es None, terminamos la recursión
        if not nodo:
            return

        # Si el número es positivo, lo insertamos en la lista de positivos
        if nodo.info > 0:
            positivos.insertar(nodo.info)
        # Si el número es negativo, lo insertamos en la lista de negativos
        elif nodo.info < 0:
            negativos.insertar(nodo.info)

        # Llamada recursiva para el siguiente nodo
        self.dividir_lista(nodo.liga_der, positivos, negativos)

# Ejemplo de uso
lista = Lista()
lista.insertar(1)
lista.insertar(-3)
lista.insertar(5)
lista.insertar(-2)
lista.insertar(4)
lista.insertar(-6)

print("Lista original:")
lista.mostrar_lista()

# Creamos dos listas vacías para los positivos y negativos
positivos = Lista()
negativos = Lista()

# Llamamos al método recursivo para dividir la lista
lista.dividir_lista(lista.p, positivos, negativos)

print("Lista de números positivos:")
positivos.mostrar_lista()

print("Lista de números negativos:")
negativos.mostrar_lista()
