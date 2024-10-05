'''Traduzca las siguientes expresiones a 
notación posfija mediante el algoritmo 3.6

a) X*(Z+W)/(T-V)
b) Z-W*Y+X^K
c) X^(Z-T)*W
d) (X-Y)*(T-Z)
e) Z/(X+Y*T)^W
f) W*(Z/(K-T))

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