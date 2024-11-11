class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def eliminar_ultimo(self):
        if self.cabeza:
            if not self.cabeza.liga:  # Si solo hay un nodo
                self.cabeza = None
            else:
                p = self.cabeza
                while p.liga and p.liga.liga:  # Busca el penúltimo nodo
                    p = p.liga
                p.liga = None  # Elimina el último nodo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.info, end=" -> ")
            actual = actual.liga
        print("None")

lista = ListaSimple()
lista.cabeza = Nodo(10)
lista.cabeza.liga = Nodo(20)
lista.cabeza.liga.liga = Nodo(30)

print("Lista original:")
lista.mostrar_lista()

lista.eliminar_ultimo()

print("Lista después de eliminar el último nodo:")
lista.mostrar_lista()
