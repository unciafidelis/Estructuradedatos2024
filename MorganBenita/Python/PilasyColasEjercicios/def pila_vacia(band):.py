def pila_vacia(band):
    # Verifica si TOPE es 0
    if band == 0:
       band = True
    else:
        band = False
        return band  # La pila no está vacía
    
print(pila_vacia(0))