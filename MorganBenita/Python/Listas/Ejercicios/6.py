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

    def mezclar_recursivo(self, nodo1, nodo2, elementos=[]):
        # Caso base: si una lista está vacía, retornamos la otra
        if not nodo1 and not nodo2:
            return elementos

        # Recursión: extraemos el elemento y lo añadimos a la lista temporal
        if nodo1:
            elementos.append(nodo1.info)
            return self.mezclar_recursivo(nodo1.liga_der, nodo2, elementos)
        
        if nodo2:
            elementos.append(nodo2.info)
            return self.mezclar_recursivo(nodo1, nodo2.liga_der, elementos)

    def crear_lista_descendente(self, elementos):
        # Ordenamos los elementos en forma descendente
        elementos.sort(reverse=True)

        # Ahora reconstruimos la lista resultante con los elementos ordenados
        lista_resultado = Lista()
        self._reconstruir_lista(lista_resultado, elementos)
        return lista_resultado

    def _reconstruir_lista(self, lista_resultado, elementos):
        # Caso base: cuando la lista de elementos está vacía
        if not elementos:
            return
        # Inserta el primer elemento de la lista ordenada
        lista_resultado.insertar(elementos[0])
        # Llama recursivamente con el resto de los elementos
        self._reconstruir_lista(lista_resultado, elementos[1:])

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

# Mezclamos las dos listas recursivamente y obtenemos los elementos
elementos_mezclados = lista1.mezclar_recursivo(lista1.p, lista2.p)

# Creamos la lista descendente con los elementos mezclados
lista3 = lista1.crear_lista_descendente(elementos_mezclados)

print("Lista resultante de la mezcla descendente:")
lista3.mostrar_lista()
