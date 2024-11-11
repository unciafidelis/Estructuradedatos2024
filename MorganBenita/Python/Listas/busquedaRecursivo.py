'''Este algoritmo permite buscar recursivamente a un elemento con información 
X en una lista simplemente ligada que se encuentra desordenada. P es el 
apuntador al primer elemento de la lista.'''

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
            nuevo.liga = self.p
            self.p = nuevo

    def busqueda_recursiva(self, p, x):
        if not p:
            return False
        if p.info == x:
            return True
        return self.busqueda_recursiva(p.liga, x)

    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.info, end=" -> ")
            actual = actual.liga
        print("None")

# Ejemplo de uso
lista = Lista()
lista.insertar(30)
lista.insertar(10)
lista.insertar(20)
lista.insertar(40)

print("Lista desordenada:")
lista.mostrar_lista()

# Buscar un elemento de forma recursiva
resultado = lista.busqueda_recursiva(lista.p, 30)
print("¿El 30 está en la lista?", resultado)

resultado = lista.busqueda_recursiva(lista.p, 50)
print("¿El 50 está en la lista?", resultado)
