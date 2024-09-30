#Este algoritmo determina si una estructura de datos tipo cola está vacía,
#asignando a BAND el valor de verdad correspondiente.

def cola_vacia(frente):
    if frente == 0:
        return True
    else:
        return False

frente = 0
band = cola_vacia(frente)
print("La cola esta vacia",band)    