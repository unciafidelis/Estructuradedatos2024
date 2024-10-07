'''Traduzca las siguientes expresiones a 
notación posfija mediante el algoritmo 3.6

a) X*(Z+W)/(T-V)
b) Z-W*Y+X^K
c) X^(Z-T)*W
d) (X-Y)*(T-Z)
e) Z/(X+Y*T)^W
f) W*(Z/(K-T))

PREFIJO
Hacer TOPE = 0
Mientras (EI sea diferente de la cadena vacía) Repetir
Tomar el símbolo más a la derecha de EI recortando 
luego la expresión
Si (el símbolo es paréntesis derecho)
entonces {Poner símbolo en pila}
Llamar a Pone con PILA, TOPE, MAX y símbolo
si no
Si (símbolo es paréntesis izquierdo)
entonces
Mientras (PILA[TOPE] != paréntesis derecho) Repetir
Llamar a Quita con PILA, TOPE y DATO
Hacer EPRE = EPRE + DATO
{Fin del ciclo}
{Sacamos el paréntesis derecho de PILA y no se agrega a EPRE}
Llamar a Quita con PILA, TOPE y DATO
si no
Si (símbolo es un operando)
entonces
Agregar símbolo a EPRE
'''

'''
POSFIJO
{Este algoritmo traduce una expresión infija -EI- a postfija -EPOS-, 
haciendo uso de una pila PILA. MAX es el número máximo de elementos 
que puede almacenar la pila}
Hacer TOPE = O
Mientras (EI sea diferente de la cadena vacía) Repetir
Tomar el símbolo más a la izquierda de EI. 
Recortar luego la expresión
Si (el símbolo es paréntesis izquierdo)
entonces {Poner símbolo en PILA. Se asume que hay espacio en PILA}
Llamar a Pone con PILA, TOPE, MAX y símbolo
si no
Si (el símbolo es paréntesis derecho)
entonces
Mientras (PILA[TOPE] != paréntesis izquierdo) Repetir
Llamar a Quita con PILA, TOPE y DATO
Hacer EPOS = EPOS + DATO
{Fin del ciclo}
Llamar a Quita con PILA, TOPE y DATO
{Se quita el paréntesis izquierdo de PILA y no se agrega
a EPaS}
si no
Si (el símbolo es un operando)
entonces
Agregar símbolo a EPaS
si no {Es un operador}
Llamar Pila_vacía con PILA, TOPE y BAND
Mientras (BAND == FALSO) y (la prioridad del
operador sea menor o igual que la prioridad
del operador que está en la cima de PILA)
Repetir
Llamar a Quita con PILA, TOPE y DATO
Hacer EPaS = EPaS + DATO
Llamar a Pila_vacía con PILA, TOPE y BAND
{Fin del ciclo}
Llamar a Pone con PILA, TOPE, MAX y símbolo
{Fin del condicional}
{Fin del condicional}
{Fin del condicional}
{Fin del ciclo}
Llamar a Pila_vacía con PILA, TOPE y BAND
Mientras (BAND == FALSO) Repetir
Llamar a Quita con PILA, TOPE YDATO
Hacer EPaS = EPaS + DATO
Llamar a Pila_vacía con PILA, TOPE y BAND
{Fin del ciclo}
Escribir EPaS
'''

'''
PONE(PILA, TOPE, MAX, DATO)
Llamar a Pila_llena con PILA, TOPE, MAX YBAND
Si (BAND = VERDADERO)
entonces
Escribir "Desbordamiento - Pila llena"
si no
Hacer TOPE = TOPE + 1 y PILA[TOPE] = DATO
{Actualiza TOPE e inserta el nuevo elemento en el TOPE de PILA}

3. {Fin del condicional del paso 2}
'''

'''
QUITA(PILA, TOPE, DATO)
Llamar a Pila_vacía con PILA, TOPE y BAND
Si (BAND = VERDADERO)
entonces
Escribir "Subdesbordarniento - Pila vacía"
si no
Hacer DATO= PILA[TOPE] y TOPE = TOPE - 1 {Actualiza TOPE}
{Fin del condicional del paso 2}
'''
'''
Pila_vacia
Si (TOPE =O) (Verifica si no hay elementos almacenados en la pila)
entonces
Hacer BAND = VERDADERO (La pila está vacía)
si no
Hacer BAND = FALSO (La pila no está vacía)
(Fin del condicional del paso 1)

'''
'''
Pila_Llena
Si (TOPE = MAX)
entonces
Hacer BAND = VERDADERO (La pila está llena)
si no
Hacer BAND = FALSO (La pila no está llena)
(Fin del condicional del paso 1)
'''

def pone(pila, tope, max, dato):
    if tope == max - 1:
        print("Desbordamiento - Pila llena")
    else:
        tope += 1
        pila[tope] = dato
    return tope

def quita(pila, tope):
    if tope == -1:
        print("Subdesbordamiento - Pila vacía")
        return None, tope
    else:
        dato = pila[tope]
        tope -= 1
        return dato, tope
    
def prioridadOperador(op):
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    if op == '^':
        return 3
    return 0

def esOperador(op):
    return op in ['+', '-', '*', '/', '^']

def infija_a_posfija(EI):
    pila = [''] * 20
    tope = -1
    EPOS = ""  
    max = 20
    
    for simbolo in EI:
        if simbolo.isalnum():  
            EPOS += simbolo
        elif simbolo == '(':
            tope = pone(pila, tope, max, simbolo)
        elif simbolo == ')':
            while pila[tope] != '(':
                dato, tope = quita(pila, tope)
                EPOS += dato
            _, tope = quita(pila, tope)
        elif esOperador(simbolo):
            while (tope != -1 and prioridadOperador(pila[tope]) >= prioridadOperador(simbolo)):
                dato, tope = quita(pila, tope)
                EPOS += dato
            tope = pone(pila, tope, max, simbolo)
    
    while tope != -1:
        dato, tope = quita(pila, tope)
        EPOS += dato

    return EPOS

expresion = "(X+Z)*W/T^Y-V"
print("Expresión infija:", expresion)
expresion_posfija = infija_a_posfija(expresion)
print("Expresión posfija:", expresion_posfija)

'''
band = False
while(EI!=''):
    dato = EI[0] 
    if dato == '(':
        print(dato)
        pila[tope] = dato
        pone(pila, tope, max, dato)
    elif dato == ')':
        while(pila[tope] != '('):
            quita(pila,tope,dato,band)
        EPOS = EPOS + dato
        quita(pila,tope,dato,band)
    elif dato != '*' or dato != '+' or dato != '/' or dato != '-':
        EPOS = EPOS + dato
    else:
        pila_vacia(pila, tope, band)
    while(band == False):
        prioridad = prioridadOperador(EI)
        if prioridad == 3:
            quita(pila,tope,dato,band)
            EPOS = EPOS + dato
        elif prioridad == 2:
            quita(pila,tope,EI,band)
            EPOS = EPOS + dato
        else:
            quita(pila,tope,EI,band)
            EPOS = EPOS + dato
        pila_vacia(pila,tope,band)
    pone(pila,tope,max,dato)

pila_vacia(pila,tope,band)
while (band == False):
    quita(pila,tope,dato,band)
    EPOS = EPOS + dato
    pila_vacia(pila,tope,band)
print(EPOS)
'''
