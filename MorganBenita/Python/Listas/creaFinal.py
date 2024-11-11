'''
Este algoritmo permite crear una lista simplemente ligada, 
agregando cada nuevo nodo al final de la misma.
P, Q y T son variables tipo apuntador. Los campos del nodo son INFO,
que será del tipo de datos que se quiera almacenar en la
lista y LIGA de tipo apuntador. P apunta al inicio de la lista. RES es
una variable de tipo entero.
'''
class Nodo:
    def __init__(self, info):
        self.info = info 
        self.liga = None  

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def crear_lista(self):
        info = int(input("Ingrese el valor para el primer nodo: "))
        self.cabeza = Nodo(info)
        
        res = int(input("Desea ingresar más nodos a la lista? Sí: 1, No: 0: "))
        
        while res == 1:
            info = int(input("Ingrese el valor para el siguiente nodo: "))
            nuevo_nodo = Nodo(info)
            
            if self.cabeza is None:
                self.cabeza = nuevo_nodo
            else:
                actual = self.cabeza
                while actual.liga is not None:  
                    actual = actual.liga
                actual.liga = nuevo_nodo  
            
            res = int(input("Desea ingresar más nodos a la lista? Sí: 1, No: 0: "))

    def imprimir_lista(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.info, end=" -> ")
            actual = actual.liga
        print("None")

lista = ListaSimple()
lista.crear_lista()
print("Lista simplemente ligada:")
lista.imprimir_lista()

