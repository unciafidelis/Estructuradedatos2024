# Ejemplo 3.1
class Pila:
    def __init__(self):
        self.elementos = []  # Inicializa la lista para almacenar elementos

    def apilar(self, dato):
        """Agrega un elemento a la cima de la pila."""
        self.elementos.append(dato)
        print(f"Apilando: {dato}")

    def desapilar(self):
        """Elimina y retorna el elemento en la cima de la pila."""
        if not self.esta_vacia():
            elemento = self.elementos.pop()
            print(f"Desapilando: {elemento}")
            return elemento
        else:
            print("Subdesbordamiento - Pila vacía")
            return None

    def cima(self):
        """Retorna el elemento en la cima de la pila sin eliminarlo."""
        if not self.esta_vacia():
            return self.elementos[-1]
        else:
            print("La pila está vacía.")
            return None

    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.elementos) == 0

    def mostrar(self):
        """Muestra los elementos de la pila."""
        print("Elementos en la pila:", self.elementos)


# Ejemplo de uso
pila = Pila()

# Insertar elementos
pila.apilar("lunes")
pila.apilar("martes")
pila.apilar("miercoles")
pila.apilar("jueves")
pila.apilar("viernes")

# Mostrar la pila
pila.mostrar()

# Desapilar el elemento "viernes"
pila.desapilar()
pila.mostrar()

# Intentar eliminar el elemento "martes"
# Para hacerlo, primero debemos desapilar "jueves" y "miercoles"
pila.desapilar()  # Elimina "jueves"
pila.desapilar()  # Elimina "miercoles"

# Ahora podemos eliminar "martes"
pila.desapilar()  # Elimina "martes"
pila.mostrar()
