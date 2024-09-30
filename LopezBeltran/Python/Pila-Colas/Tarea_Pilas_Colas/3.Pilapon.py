def pila_llena(pila, tope, MAX):
    return tope == MAX - 1
    
def agregar_elemento(pila, tope, MAX, dato):
    if pila_llena(pila, tope, MAX):
        print("Desbordamiento de pila")
    else:
        tope += 1
        if tope < len(pila):
            pila[tope] = dato  
        else:
            pila.append(dato)
    return tope

MAX = 5
pila = [None] * MAX
tope = -1 
for i in range(6):
    dato = input("Dato a insertar: ")
    tope = agregar_elemento(pila, tope, MAX, dato)

print("Contenido de la pila:", pila)
