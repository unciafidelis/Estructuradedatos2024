class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga_der = None
        self.liga_izq = None

class ListaDoble:
    def __init__(self):
        self.p = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.p:  # Si la lista está vacía, el primer nodo será el nuevo nodo
            self.p = nuevo_nodo
        else:
            actual = self.p
            while actual.liga_der:  # Avanzamos hasta el último nodo
                actual = actual.liga_der
            actual.liga_der = nuevo_nodo  # Inserta el nodo al final
            nuevo_nodo.liga_izq = actual  # Establece el enlace inverso

    def buscar_recursivo(self, nodo, x):
        # Caso base: si el nodo es None, significa que no encontramos el elemento
        if not nodo:
            return False
        # Si encontramos el valor, retornamos True
        if nodo.info == x:
            return True
        # Llamada recursiva para buscar en el siguiente nodo
        return self.buscar_recursivo(nodo.liga_der, x)

# Ejemplo de uso
lista = ListaDoble()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.insertar(40)

# Imprimir los resultados de búsqueda
print("Buscando 20 en la lista:", lista.buscar_recursivo(lista.p, 20))  # Debe retornar True
print("Buscando 50 en la lista:", lista.buscar_recursivo(lista.p, 50))  # Debe retornar False
