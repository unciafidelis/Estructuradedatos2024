# Programa de algoritmo Pila llena
pila = [] # Declaramos la pila 
tope = 0 # inicalizamos el tope en 0
band = None # band lo inicializamos none
MAX = 3 # definimos el numero maximo de elementos en la pila
pila.append(10) # agregamos elementos
tope +=1        # incrementamos el contador tope
pila.append(20)
tope +=1
pila.append(30)
tope +=1
if tope == MAX: # comprovamos si  tope es igual al valor maximo
    band = True # band le asiganamos verdadero
    print("Pila llena") # imprimimos mensaje
else: # de lo contrario
    band= False # band le asignamos falso
    print("La Pila no esta llena")    # imprimimos mensaje 
