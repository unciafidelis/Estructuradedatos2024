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
    if op == '^':
        return 3
    return 0

def conv_prefija(EI):
    EI = EI[::-1]  # Invertir la expresión
    max_size = len(EI)  # Definir el tamaño máximo de la pila
    pila = Pila(max_size)
    epre = ""
    
    for simbolo in EI:
        if simbolo == ')':
            pila.poner(simbolo)
        elif simbolo == '(':
            while not pila.es_vacia() and pila.cima() != ')':
                epre += pila.quitar()
            pila.quitar()  # Quitar el paréntesis derecho
        elif simbolo.isalnum():  # Operando (número o letra)
            epre += simbolo
        else:  # Operador
            while (not pila.es_vacia() and 
                   prioridad(simbolo) < prioridad(pila.cima())):
                epre += pila.quitar()
            pila.poner(simbolo)
    
    # Vaciar la pila al final
    while not pila.es_vacia():
        epre += pila.quitar()
    
    return epre[::-1]  # Invertir el resultado final

# Ejemplo de uso
expresion_infixa =input("Ingrese expresion\n")
resultado = conv_prefija(expresion_infixa)
print(f"Expresión prefija: {resultado}")
