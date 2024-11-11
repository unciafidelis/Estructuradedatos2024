'''Este algoritmo permite buscar el elemento con información X en una lista 
simplemente ligada que se encuentra ordenada en forma ascendente. P es el 
apuntador al primer nodo de la lista. Q es una variable de tipo apuntador. 
Info y Liga son los campos de los nodos de la lista.'''

class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

class Lista:
    def __init__(self):
        self.p = None

    def insertar(self, info):
        nuevo = Nodo(info)
        if not self.p:
            self.p = nuevo
        else:
            actual = self.p
            while actual.liga:
                actual = actual.liga
            actual.liga = nuevo

    def busqueda_ordenada(self, x):
        actual = self.p
        while actual and actual.info <= x:
            if actual.info == x:
                return True
            actual = actual.liga
        return False

    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.info, end=" -> ")
            actual = actual.liga
        print("None")

# Ejemplo de uso
lista = Lista()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.insertar(40)

print("Lista ordenada:")
lista.mostrar_lista()

# Buscar un elemento
resultado = lista.busqueda_ordenada(30)
print("¿El 30 está en la lista?", resultado)

resultado = lista.busqueda_ordenada(50)
print("¿El 50 está en la lista?", resultado)
