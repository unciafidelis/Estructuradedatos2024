class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga_der = None  # Puntero al siguiente nodo
        self.liga_izq = None  # Puntero al nodo anterior

class ListaDoble:
    def __init__(self):
        self.p = None  # Primer nodo de la lista
        self.f = None  # Último nodo de la lista

    # Insertar un nodo al final de la lista doblemente ligada
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.p:
            self.p = nuevo_nodo  # El primer nodo es el nuevo nodo
            self.f = nuevo_nodo  # El último nodo también es el nuevo nodo
        else:
            self.f.liga_der = nuevo_nodo  # El nodo anterior apunta al nuevo nodo
            nuevo_nodo.liga_izq = self.f  # El nuevo nodo apunta al nodo anterior
            self.f = nuevo_nodo  # El nuevo nodo se convierte en el último nodo

    # Recorrido recursivo de adelante hacia atrás
    def recorrer_adelante(self, nodo):
        if nodo is not None:  # Si el nodo no es None
            print(nodo.info, end=" -> ")
            self.recorrer_adelante(nodo.liga_der)  # Llamada recursiva al siguiente nodo

    # Recorrido recursivo de atrás hacia adelante
    def recorrer_atras(self, nodo):
        if nodo is not None:  # Si el nodo no es None
            print(nodo.info, end=" -> ")
            self.recorrer_atras(nodo.liga_izq)  # Llamada recursiva al nodo anterior

    # Método para iniciar el recorrido hacia adelante
    def mostrar_lista_adelante(self):
        print("Recorrido hacia adelante: ", end="")
        self.recorrer_adelante(self.p)  # Empezamos desde el primer nodo
        print("None")

    # Método para iniciar el recorrido hacia atrás
    def mostrar_lista_atras(self):
        print("Recorrido hacia atrás: ", end="")
        self.recorrer_atras(self.f)  # Empezamos desde el último nodo
        print("None")

# Ejemplo de uso
lista = ListaDoble()

# Insertamos elementos en la lista
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.insertar(40)

# Mostramos la lista recursivamente en ambos sentidos
lista.mostrar_lista_adelante()  # Recorrido de adelante hacia atrás
lista.mostrar_lista_atras()     # Recorrido de atrás hacia adelante
