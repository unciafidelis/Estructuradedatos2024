'''Este subprograma mezcla dos listas ordenadas y forma una tercera lista 
ordenada. P y Q son apuntadores a las dos listas ordenadas de entrada y la 
lista resultante está formada por la mezcla de ambas.'''

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

    def mezcla_ordenada(self, lista2):
        lista_resultado = Lista()
        actual1 = self.p
        actual2 = lista2.p

        while actual1 and actual2:
            if actual1.info <= actual2.info:
                lista_resultado.insertar(actual1.info)
                actual1 = actual1.liga_der
            else:
                lista_resultado.insertar(actual2.info)
                actual2 = actual2.liga_der

        while actual1:
            lista_resultado.insertar(actual1.info)
            actual1 = actual1.liga_der

        while actual2:
            lista_resultado.insertar(actual2.info)
            actual2 = actual2.liga_der

        return lista_resultado

# Ejemplo de uso
lista1 = Lista()
lista1.insertar(1)
lista1.insertar(3)
lista1.insertar(5)

lista2 = Lista()
lista2.insertar(2)
lista2.insertar(4)
lista2.insertar(6)

print("Lista 1:")
lista1.mostrar_lista()

print("Lista 2:")
lista2.mostrar_lista()

lista3 = lista1.mezcla_ordenada(lista2)

print("Lista resultante de la mezcla ordenada:")
lista3.mostrar_lista()
