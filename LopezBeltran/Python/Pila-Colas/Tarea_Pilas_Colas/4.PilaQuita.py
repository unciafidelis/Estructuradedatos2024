pila = []
tope = 0
band = None

def pila_vacia():   
    if tope == len(pila):
        print("Pila vacia")
        band= True
    else:
        band = False
    return band    

if band == True:
    print("Subdesbordamiento - pila vacia")
else:
    dato = int(input("Ingrese dato "))
    pila.append(dato)
    tope -= 1

print("Datos en pila",pila)


