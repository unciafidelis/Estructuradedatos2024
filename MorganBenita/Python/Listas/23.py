class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimplementeLigada:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def completar_numeros_faltantes(self):
        actual = self.cabeza
        while actual and actual.siguiente:
            siguiente_valor = actual.siguiente.dato
            actual_valor = actual.dato
            # Si hay una diferencia mayor a 1 entre nodos consecutivos
            if siguiente_valor - actual_valor > 1:
                # Crear e insertar los nodos faltantes
                for valor in range(actual_valor + 1, siguiente_valor):
                    nuevo_nodo = Nodo(valor)
                    nuevo_nodo.siguiente = actual.siguiente
                    actual.siguiente = nuevo_nodo
                    actual = nuevo_nodo
            actual = actual.siguiente

# Ejemplo de uso
lista = ListaSimplementeLigada()
lista.insertar_final(12)
lista.insertar_final(13)
lista.insertar_final(15)
lista.insertar_final(18)

print("Lista original:")
lista.mostrar_lista()

# Completar los números faltantes
lista.completar_numeros_faltantes()

print("Lista después de completar los números faltantes:")
lista.mostrar_lista()
