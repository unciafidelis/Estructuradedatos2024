#Algoritmo 12 Elimina_circular
#Este algoritmo elimina el primer elemento de una estructura tipo cola circular y lo almacena en DATO.   
def elimina_circular(colacir, maximo, frente, final):
    # Verificar si la cola está vacía
    if frente == 0:
        print("Subdesbordamiento - Cola vacía")
        return None, frente, final  # Retorna None si está vacía

    # Almacenar el elemento a eliminar
    dato = colacir[frente - 1]  # -1 porque los índices en Python comienzan en 0

    # Verificar si hay solo un elemento
    if frente == final:
        frente = 0  # Reiniciar cola
        final = 0
    else:
        # Ajustar el índice de FRENTE
        if frente == maximo:
            frente = 1
        else:
            frente += 1

    return dato, frente, final

# Ejemplo de uso
maximo = 5
colacir = [10, None, None, None, None]  # Cola circular con un elemento
frente = 1  # Indica que hay un elemento
final = 1

# Eliminar un dato
dato, frente, final = elimina_circular(colacir, maximo, frente, final)
if dato is not None:
    print("Elemento eliminado:", dato)
print("Cola circular después de eliminar:", colacir)
print("Frente:", frente, "Final:", final)
