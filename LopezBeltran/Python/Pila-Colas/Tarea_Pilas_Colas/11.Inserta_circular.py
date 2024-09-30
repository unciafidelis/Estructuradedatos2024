#Algoritmo 3.11 Inserta_circular
#Este algoritmo inserta el elemento DATO al final de una estructura de tipo cola circular.
def inserta_circular(colacir, maximo, frente, final, dato):
    # Verificar si la cola está llena
    if (final == maximo and frente == 1) or (final + 1 == frente):
        print("Desbordamiento - Cola llena")
    else:
        # Ajustar el índice de FINAL
        if final == maximo:
            final = 1
        else:
            final += 1
        
        # Insertar el dato
        colacir[final - 1] = dato  # -1 porque los índices en Python comienzan en 0
        
        # Ajustar el frente si es necesario
        if frente == 0:
            frente = 1
    
    return frente, final

# Ejemplo de uso
maximo = 5
colacir = [None] * maximo  # Inicializa la cola circular
frente = 0
final = 0

# Insertar un dato
dato = 10
frente, final = inserta_circular(colacir, maximo, frente, final, dato)
print("Cola circular después de insertar:", colacir)
print("Frente:", frente, "Final:", final)
