class Postres:
    def __init__(self):
        self.postres = {}  # Diccionario para almacenar postres y sus ingredientes
    
    # Imprimir los ingredientes de un postre dado su nombre
    def imprimir_ingredientes(self, nombre_postre):
        if nombre_postre in self.postres:
            print(f"Ingredientes de {nombre_postre}: {', '.join(self.postres[nombre_postre])}")
        else:
            print(f"El postre {nombre_postre} no está registrado.")
    
    # Insertar nuevos ingredientes en un postre
    def insertar_ingredientes(self, nombre_postre, ingredientes):
        if nombre_postre in self.postres:
            self.postres[nombre_postre].extend(ingredientes)
            print(f"Ingredientes añadidos a {nombre_postre}.")
        else:
            print(f"El postre {nombre_postre} no existe. Utilice el método de alta para registrarlo.")
    
    # Eliminar un ingrediente de un postre
    def eliminar_ingrediente(self, nombre_postre, ingrediente):
        if nombre_postre in self.postres:
            if ingrediente in self.postres[nombre_postre]:
                self.postres[nombre_postre].remove(ingrediente)
                print(f"Ingrediente {ingrediente} eliminado de {nombre_postre}.")
            else:
                print(f"El ingrediente {ingrediente} no existe en el postre {nombre_postre}.")
        else:
            print(f"El postre {nombre_postre} no está registrado.")
    
    # Dar de alta un postre con todos los ingredientes
    def alta_postre(self, nombre_postre, ingredientes):
        if nombre_postre not in self.postres:
            self.postres[nombre_postre] = ingredientes
            print(f"El postre {nombre_postre} ha sido dado de alta con los ingredientes {', '.join(ingredientes)}.")
        else:
            print(f"El postre {nombre_postre} ya existe.")
    
    # Dar de baja un postre con todos sus ingredientes
    def baja_postre(self, nombre_postre):
        if nombre_postre in self.postres:
            del self.postres[nombre_postre]
            print(f"El postre {nombre_postre} ha sido dado de baja.")
        else:
            print(f"El postre {nombre_postre} no está registrado.")

# Ejemplo de uso

# Crear una instancia de la clase Postres
postres_manager = Postres()

# Dar de alta un postre
postres_manager.alta_postre("Pastel de Chocolate", ["chocolate", "harina", "azúcar", "huevo"])

# Imprimir ingredientes de un postre
postres_manager.imprimir_ingredientes("Pastel de Chocolate")

# Insertar nuevos ingredientes en un postre
postres_manager.insertar_ingredientes("Pastel de Chocolate", ["vainilla", "mantequilla"])

# Imprimir ingredientes de un postre después de añadir ingredientes
postres_manager.imprimir_ingredientes("Pastel de Chocolate")

# Eliminar un ingrediente de un postre
postres_manager.eliminar_ingrediente("Pastel de Chocolate", "azúcar")

# Imprimir ingredientes de un postre después de eliminar un ingrediente
postres_manager.imprimir_ingredientes("Pastel de Chocolate")

# Dar de baja un postre
postres_manager.baja_postre("Pastel de Chocolate")

# Intentar imprimir ingredientes de un postre que fue dado de baja
postres_manager.imprimir_ingredientes("Pastel de Chocolate")
