class Pila:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = []
        
    def es_vacia(self):
        return len(self.items) == 0
    
    def poner(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
    
    def quitar(self):
        if not self.es_vacia():
            return self.items.pop()
    
    def cima(self):
        if not self.es_vacia():
            return self.items[-1]
        
def prioridad(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def conv_postfija(EI):
    max_size = len(EI)  # Definir el tamaño máximo de la pila
    pila = Pila(max_size)
    epos = ""
    
    for simbolo in EI:
        if simbolo == '(':
            pila.poner(simbolo)
        elif simbolo == ')':
            while not pila.es_vacia() and pila.cima() != '(':
                epos += pila.quitar()
            pila.quitar()  # Quitar el paréntesis izquierdo
        elif simbolo.isalnum():  # Operando (número o letra)
            epos += simbolo
        else:  # Operador
            while (not pila.es_vacia() and 
                   prioridad(simbolo) <= prioridad(pila.cima())):
                epos += pila.quitar()
            pila.poner(simbolo)
    
    # Vaciar la pila al final
    while not pila.es_vacia():
        epos += pila.quitar()
    
    return epos

# Ejemplo de uso
expresion_infija =input("Ingrese La Exprecion\n")
resultado = conv_postfija(expresion_infija)
print(f"Expresión postfija: {resultado}")
