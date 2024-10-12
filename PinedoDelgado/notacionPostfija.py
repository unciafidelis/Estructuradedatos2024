'''Traduzca la siguioente expresiones en notación postfija el algoritmo3.6'''
'''
A) X-(Z+W)/(T-V)
B) Z-W*Y+X^K
C) X^(Z-T)W
D) (X-Y)*(T-Z)
E) Z/(X+Y*T)^W
F) W*(Z/(K-T))

Hacer TOPE = 0
Hacer TOPE ....... O
... Mientras (El sea diferente de la cadena vacía) Repetir
Tomar el símbolo más a la derecha de El recortando luego la expresión
_.1 Si (el símbolo es paréntesis derecho)
entonces {Poner símbolo en pila}
Llamar a Pone con PILA, TOPE, MAX Ysímbolo
si no
2 1 Si (símbolo es paréntesis izquierdo)
entonces
21. .1 Mientras (pILA[TOPE] .. paréntesis derecho) Repetir
Llamar a Quita con PILA, TOPE YDATO
Hacer EPRE = EPRE + DATO
{Fin del ciclo}
{Sacamos el paréntesis derecho de PILA y no se agrega a EPRE}
Llamar a Quita con PILA, TOPE YDATO
si no
Si (símbolo es un operando)
entonces
Agregar símbolo a EPR

'''
'''
PONE
Pone (PILA, TOPE, MAX, DATO)

l. Llamar a Pila_llena con PILA, TOPE, MAX YBAND
2. Si (BAND = VERDADERO)
entonces
Escribir "Desbordamiento - Pila llena"
si no
Hacer TOPE +- TOPE + 1 y PILA[TOPE] +- DATO
{Actualiza TOPE e inserta el nuevo elemento en el TOPE de PILA}
3. {Fin del condicional del paso 2}
'''

'''
QUITA
Quita (PILA, TOPE, DATO)
1. Llamar a Pila_vacía con PILA, TOPE YBAND
2. Si (BAND = VERDADERO)
entonces
Escribir "Subdesbordarniento - Pila vacía"
si no
Hacer DATO = PILA [TOPE] Y TOPE = TOPE - 1 {Actualiza TOPE}
3. {Fin del condicional del paso 2}
'''
'''
PILA VACIA
Pila_vaCla (PILA, TOPE, BANm
Si (TOPE =O) (Verifica si no hay elementos almacenados en la pila)
entonces
Hacer BAND oE- VERDADERO (La pila está vacía)
si no
Hacer BAND oE- FALSO (La pila no está vacía)
(Fin del condicional del paso 1
'''

'''
PILA LLENA
Pila_llena (PILA, TOPE, MAX, BAND)
Si (TOPE =MAX)
entonces
Hacer BAND oE- VERDADERO (La pila está llena)
si no
Hacer BAND oE- FALSO (La pila no está llena)
¿. (Fin del condicional del paso 1
'''
#algoritmo pila llena
def pila_llena(pila, tope, max, band):
    if tope == max:
        band = True  # La pila está llena
    else:
        band = False  # La pila no está llena
#algoritmo pila vacía
def pila_vacia(pila, tope, band):
    # Verifica si TOPE es 0
    if tope == 0:
        band = True  # La pila está vacía
    else:
        band = False  # La pila no está vacía
#ALGORITMO PONE
def pone(pila, tope, max, dato):
    band = None
    pila_llena(pila, tope, max, band)
    if band==True:  
         print("Desbordamiento - Pila llena")
    else:
        tope += 1  
        pila[tope] = dato  
#ALGORITMO QUITA
def quita(pila, tope, dato, band):
    pila_vacia(pila, tope, band)

    if band == True: 
        print("Subdesbordamiento - Pila vacía")
    else:
        dato = pila[tope]  
        tope -= 1

def prioridad(op):
    if op in ['+','-']:
        return 1
    if op in ['*','/']:
        return 2
    

        


TOPE = 0
pila = []

EI = 'X-(Z+W)/(T-V)'
EI=EI[-1] #el simbolo más a la derecha y recortas
while(EI!=''):
    if(EI):
        pila = [TOPE]=EI
print(EI)