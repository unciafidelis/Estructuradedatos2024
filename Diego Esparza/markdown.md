:smile: :rocket: :+1:
## Diego Ricardo Esparza Cortes
### Estructura de datos
---

## 3.1 Introducción a Pilas y Colas

En el primer capítulo, se discutieron los arreglos como estructuras lineales, donde cada elemento tiene un único sucesor y un único predecesor, excepto el primer y el último elemento, respectivamente. Al analizar las operaciones de inserción y eliminación, se destacó que los elementos pueden ser añadidos o eliminados desde cualquier posición del arreglo. Sin embargo, hay problemas que requieren que las inserciones y eliminaciones se realicen exclusivamente desde un extremo.
***
# Algoritmo 3.1
## Verificar_Pila_Vacía (PILA, TOPE, BAND)

### Descripción
Este algoritmo determina si una estructura de tipo pila llamada `PILA` se encuentra vacía, estableciendo en `BAND` el valor booleano adecuado. La pila se organiza mediante un arreglo unidimensional. `TOPE` es un argumento de tipo entero, y `BAND` es un argumento de tipo booleano.

1. Si (`TOPE == 0`) {Verifica la ausencia de elementos en la pila} 
   - *entonces*
       - Asignar `BAND <- VERDADERO` {La pila se encuentra vacía}
   - *de lo contrario*
       - Asignar `BAND <- FALSO` {La pila contiene elementos}
2. {Fin del condicional del paso 1}

### Código
```python
def verificar_pila_vacia(pila, tope, band):
    # Comprobar si TOPE es 0
    if tope == 0:
        band = True  # Indica que la pila está vacía
    else:
        band = False  # Indica que la pila tiene elementos
```
***
# Algoritmo 3.2
## Comprobar_Pila_Llena (PILA, TOPE, MAX, BAND)

### Descripción
Este algoritmo determina si una estructura de tipo pila denominada `PILA` está completamente llena, asignando a `BAND` el valor booleano correspondiente. La pila se implementa mediante un arreglo unidimensional que puede contener hasta `MAX` elementos. `TOPE` es un parámetro de tipo entero, mientras que `BAND` es un parámetro de tipo booleano.

### Algoritmo
1. Si (`TOPE == MAX`)
   - *entonces*
       - Asignar `BAND <- VERDADERO` {La pila está llena}
   - *de lo contrario*
       - Asignar `BAND <- FALSO` {La pila no está llena}
2. {Fin del condicional del paso 1}

### Código
```python
def comprobar_pila_llena(pila, tope, max, band):
    if tope == max:
        band = True  # La pila está llena
    else:
        band = False  # La pila no está llena
```
***
# Algoritmo 3.3
## Agregar_Elemento (PILA, TOPE, MAX, DATO)

### Descripción
Este algoritmo inserta el elemento `DATO` en una estructura de tipo pila `PILA`, siempre que esta no esté llena. Actualiza el valor de `TOPE`. `MAX` define el número máximo de elementos que `PILA` puede almacenar. `TOPE` es un parámetro de tipo entero.

### Algoritmo
1. Llamar a `Comprobar_Pila_Llena` con `PILA`, `TOPE`, `MAX` y `BAND`
2. Si (`BAND == VERDADERO`)
   - *entonces*
       - Mostrar "Desbordamiento - Pila llena"
   - *de lo contrario*
       - Asignar `TOPE <- TOPE + 1` y `PILA[TOPE] <- DATO`
       {Actualiza TOPE e inserta el nuevo elemento en la posición TOPE de `PILA`}
3. {Fin del condicional del paso 2}

### Código
```python
def agregar_elemento(pila, tope, max, dato):
    comprobar_pila_llena(pila, tope, max, band)
    if band == True:  
        print("Desbordamiento - Pila llena")
    else:
        tope += 1  
        pila[tope] = dato  
```
***
# Algoritmo 3.4
## Extraer (PILA, TOPE, DATO)

### Descripción
Este algoritmo elimina un elemento `DATO` de una estructura de tipo pila llamada `PILA`, siempre que esta no esté vacía. El elemento que se elimina es el que está en la posición indicada por `TOPE`.

### Algoritmo
1. Invocar a `Pila_vacia` con `PILA`, `TOPE` y `BAND`
2. Si (`BAND == VERDADERO`)
   - *entonces*
       - Mostrar "Subdesbordamiento - Pila vacía"
   - *de lo contrario*
       - Asignar `DATO <- PILA[TOPE]` y `TOPE <- TOPE - 1` {Actualiza TOPE}
3. {Fin del condicional del paso 2}

### Código
```python
def extraer(pila, tope, dato, band):
    pila_vacia(pila, tope, band)

    if band == True: 
        print("Subdesbordamiento - Pila vacía")
    else:
        dato = pila[tope]  
        tope -= 1  
```
---
# Ejemplo 3.1
Si se añaden los elementos *lunes, martes, miércoles, jueves y viernes* en `PILA`, . Luego, si se elimina el elemento *viernes*, el `TOPE` ahora apuntará a jueves (ver figura 3.6b).


En caso de que se desee eliminar el elemento *martes*, esto no será posible, ya que solo se puede acceder al elemento en la parte superior de la pila.

Una forma de solucionar este inconveniente es eliminando primero los elementos jueves y miércoles. Así, *martes* se situaría en la cima de `PILA`, permitiendo que se pueda extraer .
***
# Ejemplo 3.2

Este ejemplo presenta dos casos de conversión de notación infija a posfija. El primero es una expresión simple, mientras que el segundo es más complejo. Los pasos necesarios para la traducción de la primera expresión se detallan en la tabla 3.1, y los correspondientes a la segunda expresión en la tabla 3.2.

- A) Expresión infija: `X + Z * W`  
  Expresión postfija: `XZW*+`  

##### Tabla 3.1: Conversión de infija a posfija

| Pasos | Expresión      |
|-------|----------------|
| 0     | X + Z * W      |
| 1     | X + Z W *      |
| 2     | X Z W * +      |

Durante la traducción, el primer operador que se procesa es la multiplicación (paso 1) debido a su mayor prioridad. Se coloca de manera que sus operandos la precedan. Para el operador de suma, se aplica el mismo criterio, donde ambos operandos lo anteceden. En este caso, el primer operando es X y el segundo es `ZW*`.

- B) Expresión infija: `(X + Z) * W / T ^ Y - V`  
  Expresión postfija: `XZ+W*TY^/V-`

##### Tabla 3.2: Conversión de infija a posfija

| Pasos | Expresión               |
|-------|-------------------------|
| 0     | (X + Z) * W / T ^ Y - V |
| 1     | XZ + * W / T ^ Y - V    |
| 2     | XZ + * W T ^ - V        |
| 3     | XZ + W * / T Y ^ - V    |
| 4     | XZ + W * T Y ^ / - V    |
| 5     | XZ + W * T Y ^ / V -    |

En el paso 1, se convierte la subexpresión entre paréntesis por ser de mayor prioridad. Luego, se procesa el operador de potencia (paso 2) y los demás según su jerarquía. Dado que la multiplicación y la división tienen igual prioridad, se procesa primero la multiplicación por estar más a la izquierda en la expresión (paso 3). Finalmente, el operador de resta es el último en moverse (paso 5). A continuación, se presenta el algoritmo para traducir una expresión infija a otra posfija.
***
# Algoritmo 3.5

## Conv_postfija (EL, EPOS)

### Descripción
Este algoritmo traduce una expresión infija `EI` a postfija `EPOS`, utilizando una pila `PILA`. `MAX` es el número máximo de elementos que puede almacenar la pila.

### Algoritmo

1. Hacer `TOPE <- 0`
2. Mientras (`EL` sea diferente de la cadena vacía) Repetir
   - Tomar el símbolo más a la izquierda de `EL`. Recortar luego la expresión.
   - 2.1 Si (el símbolo es paréntesis izquierdo):
       - *entonces* {Poner símbolo en `PILA`. Se asume que hay espacio en `PILA`}
         - Llamar a `Pone` con `PILA`, `TOPE`, `MAX` y símbolo
       - *sino*
       - 2.1.1 Si (el símbolo es paréntesis derecho):
           - *entonces*
              - 2.1.1.1 Mientras (`PILA[TOPE] != paréntesis izquierdo`) Repetir
                - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
                - Hacer `EPOS <- EPOS + DATO`
             - 2.1.1.2 {Fin del ciclo del paso 2.1.1.1}
               - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
                {Se quita el paréntesis izquierdo de `PILA` y no se agrega a `EPOS`}
                - *si no*
             - 2.1.1.3 Si (el símbolo es un operador):
               - *entonces*
                 - Agregar símbolo a `EPOS`
               - *si no* {Es un operador}
               - Llamar `Pila_vacia` con `PILA`, `TOPE` y `BAND`
                - 2.1.1.3A Mientras (`BAND = FALSO`) y (la prioridad del operador sea <= que la prioridad del operador que está encima de `PILA`) Repetir
                   - Llamar a `Quita` con `PILA`, `TOPE`, `DATO`
                   - Hacer `EPOS <- EPOS + DATO`
                   - Llamar a `Pila_vacia` con `PILA`, `TOPE` y `BAND`
               - 2.1.1.3B {Fin del ciclo del paso 2.1.1.3A}
                   - Llamar a `Pone` con `PILA`, `TOPE` y simbolo
              - 2.1.1.4 {Fin del condicional del paso 2.1.1.3}
      - 2.1.2 {Fin del condicional del paso 2.1.1}
    - 2.2 {Fin del condicional del paso 2.1}
3. {Fin del ciclo del paso 2}
4. Llamar `Pila_vacia` con `PILA`, `TOPE` y `BAND`
5. Mientras (`BAND = FALSO`) Repetir:
   - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
   - Hacer `EPOS <- EPOS + DATO`
   - Llamar a `Pila_vacia` con `PILA`, `TOPE` y `BAND`
6. {Fin del ciclo del paso 5}
7. Escribe `EPOS`

***
# Ejemplo 3.3
En este ejemplo se retoman los casos del ejemplo 3.2 para ilustrar el funcionamiento del algoritmo Conv_posfija.

## A) Expresión infija: `X + Z * W`  
**Expresión postfija:** `XZW*+`

En la tabla 3.3 se presentan los pasos necesarios para lograr la traducción deseada siguiendo el algoritmo 3.5.

### Tabla 3.3: Traducción de infija a postfija

| Pasos | EL        | Símbolo analizado | Pila | EPOS  |
|-------|-----------|-------------------|------|-------|
| 0     | X + Z * W |                   |      |       |
| 1     | + Z * W   | X                 |      | X     |
| 2     | Z * W     | +                 | +    | X     |
| 3     | * W       | Z                 | +    | XZ    |
| 4     | W         | *                 | + *  | XZ    |
| 5     |           | W                 | + *  | XZW   |
| 6     |           |                   | +    | XZW*  |
| 7     |           |                   |      | XZW*+ |

**Descripción**:
- En los pasos 1, 3 y 5, los operandos se agregan directamente a `EPOS`.
- En el paso 2, el operador `+` se pone en la pila porque está vacía.
- En el paso 4, el operador `*` también se agrega a la pila porque tiene mayor prioridad que `+`.
- Finalmente, en los pasos 6 y 7, se extraen los operadores de la pila y se añaden a `EPOS`.

## B) Expresión infija: `(X + Z) * W / T ^ Y - V`  
**Expresión postfija:** `XZ+W*TY^/V-`

En la tabla 3.4 se presentan los pasos necesarios para lograr la traducción deseada siguiendo el algoritmo 3.5.

### Tabla 3.4: Traducción de infija a postfija

| Pasos | EL              | Símbolo analizado  | Pila  | EPOS         |
|-------|-----------------|--------------------|-------|--------------|
| 0     | (X + Z) * W / T ^ Y - V |                  |       |              |
| 1     | X + Z) * W / T ^ Y - V | (                | (     |              |
| 2     | + Z) * W / T ^ Y - V    | X                | (     | X            |
| 3     | Z) * W / T ^ Y - V      | +                | (+    | X            |
| 4     | ) * W / T ^ Y - V       | Z                | (+    | XZ           |
| 5     | * W / T ^ Y - V         | )                | (     | XZ+          |
|       |                         | )                |       | XZ+          |
| 6     | W / T ^ Y - V           | *                | *     | XZ+          |
| 7     | / T ^ Y - V             | W                | *     | XZ+W         |
| 8     | T ^ Y - V               | /                | /     | XZ+W*        |
| 9     | ^ Y - V                 | T                | /     | XZ+W*T       |
| 10    | Y - V                   | ^                | /^    | XZ+W*T       |
| 11    | - V                     | Y                | /^    | XZ+W*TY      |
|       |                         | -                | /     | XZ+W*TY^     |
| 12    | V                       | -                | -     | XZ+W*TY^/    |
|       |                         | -                | -     | XZ+W*TY^/V   |
| 13    |                         | V                | -     | XZ+W*TY^/V   |
| 14    |                         |                    |       | XZ+W*TY^/V-  |

**Descripción**:
- En el paso 5, al analizar el paréntesis derecho se extraen repetidamente todos los elementos de `PILA` (en este caso solo el operador `+`), agregándolos a `EPOS` hasta encontrar un paréntesis izquierdo. El paréntesis izquierdo se quita de `PILA` pero no se incluye en `EPOS`.
- Cuando se trata el operador de división, en el paso 8, se quita de `PILA` el operador `*` y se agrega a `EPOS`, ya que la multiplicación tiene igual prioridad que la división.
- Al analizar el operador de resta en el paso 12, se extraen de `PILA` todos los operadores de mayor o igual prioridad, en este caso, son todos los que están en ella (la potencia y la división), agregando finalmente el símbolo en `PILA`. Luego de agregar a `EPOS` el último operando y habiendo revisado toda la expresión inicial, se vacía `PILA` y se incorporan los operadores (en este caso el operador `-`) a la expresión postfija.

***
# Ejemplo 3.4

En este ejemplo se exponen dos casos de traducción de notación infija a prefija. El primero de ellos es una expresión simple, mientras que el segundo presenta mayor grado de complejidad.

## A) Expresión infija: `X + Z * W`  
**Expresión prefija:** `+ X * Z W`

En la tabla 3.5 se presentan los pasos necesarios para lograr la traducción deseada.

### Tabla 3.5: Traducción de infija a prefija

| Pasos | EL         | Símbolo analizado | Pila     | EPREF      |
|-------|------------|-------------------|----------|------------|
| 0     | X + Z * W  |                   |          |            |
| 1     | + Z * W    | X                 |          | X          |
| 2     | Z * W      | +                 | +        | X          |
| 3     | * W        | Z                 | +        | X Z        |
| 4     | W          | *                 | + *      | X Z        |
| 5     |            | W                 | + *      | X Z W      |
| 6     |            |                   | +        | + X * Z W  |
| 7     |            |                   |          | + X * Z W  |

**Descripción**:
- En los pasos 1, 3 y 5, los operandos se agregan directamente a `EPREF`.
- En el paso 2, el operador `+` se pone en la pila.
- En el paso 4, el operador `*` se agrega a la pila.
- Finalmente, en los pasos 6 y 7, se extraen los operadores de la pila y se añaden a `EPREF`, formando la expresión prefija.

## B) Expresión infija: `(X + Z) * W / T ^ Y - V`  
**Expresión prefija:** `- / * + X Z W ^ T Y V`

En la tabla 3.6 se presentan los pasos necesarios para lograr la traducción deseada.

### Tabla 3.6: Traducción de infija a prefija

| Pasos | EL                  | Símbolo analizado  | Pila    | EPREF               |
|-------|---------------------|--------------------|---------|---------------------|
| 0     | (X + Z) * W / T ^ Y - V |                  |         |                     |
| 1     | X + Z) * W / T ^ Y - V  | (                | (       |                     |
| 2     | + Z) * W / T ^ Y - V    | X                | (       | X                   |
| 3     | Z) * W / T ^ Y - V      | +                | (+      | X                   |
| 4     | ) * W / T ^ Y - V       | Z                | (+      | X Z                 |
| 5     | * W / T ^ Y - V         | )                | (       | + X Z               |
| 6     | W / T ^ Y - V           | *                | *       | + X Z               |
| 7     | / T ^ Y - V             | W                | *       | + X Z W             |
| 8     | T ^ Y - V               | /                | /       | + X Z W *           |
| 9     | ^ Y - V                 | T                | /       | + X Z W * T         |
| 10    | Y - V                   | ^                | /^      | + X Z W * T         |
| 11    | - V                     | Y                | /^      | + X Z W * T Y       |
| 12    | V                       | -                | -       | / - + X Z W * T Y   |
| 13    |                         | V                | -       | / - + X Z W * T Y V |
| 14    |                         |                    |         | - / * + X Z W ^ T Y V |

**Descripción**:
- En el paso 5, se extraen todos los elementos de la pila hasta encontrar un paréntesis izquierdo.
- Cuando se trata el operador de división, se eliminan los operadores de mayor o igual prioridad y se añaden a `EPREF`.
- Finalmente, se agrega el operador de resta y se forma la expresión prefija final.

***
# Algoritmo 3.6

## Conv_pretfija (EL, EPRE)

### Descripción
Este algoritmo traduce una expresión en notación infija, `EL`, a prefija, `EPRE`, haciendo uso de una pila `PILA`. `TOPE` es una variable de tipo entero y `MAX` representa el máximo número de elementos que puede almacenar la pila.

### Algoritmo
1. Hacer `TOPE <- 0`
2. Mientras (`EL` sea diferente de la cadena vacía) Repetir
   - Tomar el símbolo más a la derecha de `EL` recortando luego la expresión
   - 2.1 Si (el símbolo es paréntesis derecho)
     - *entonces* {Poner símbolo en pila} 
       - Llamar a `Pone` con `PILA`, `TOPE`, `MAX` y símbolo
   - *si no*
     - 2.1.1 Si (el símbolo es paréntesis izquierdo):
       - *entonces*
         - 2.1.1.1 Mientras (`PILA[TOPE] != paréntesis derecho`) Repetir
           - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
           - Hacer `EPRE <- EPRE + DATO`
         - 2.1.1.2 {Fin del ciclo del paso 2.1.1.1}  {Sacamos el paréntesis derecho de PILA y no se agrega a EPRE}
           - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
     - *si no*
       - 2.1.1.3 Si (el símbolo es un operador):
         - *entonces*
           - Agregar símbolo a `EPRE`

***
# Algoritmo 3.7

## Inserta_cola (COLA, MAX, FRENTE, FINAL, DATO)

### Descripción
Este algoritmo inserta el elemento `DATO` al final de una estructura tipo cola. `FRENTE` y `FINAL` son los punteros que indican, respectivamente, el inicio y fin de `COLA`. La primera vez `FRENTE` y `FINAL` tienen el valor 0, ya que la cola está vacía. `MAX` es el máximo número de elementos que puede almacenar la cola.

### Algoritmo
1. Si (`FINAL < MAX`) {Verifica que hay espacio libre}
   - *entonces*
     - Hacer `FINAL <- FINAL + 1` {Actualiza `FINAL`} y `COLA[FINAL] <- DATO`
     - 1.1 Si (`FINAL = 1`) *entonces* {Se insertó el primer elemento de `COLA`}
       - Hacer `FRENTE <- 1`
     - 1.2 {Fin del condicional del paso 1.1}
   - *si no*
     - Escribir "Desbordamiento - Cola llena"
2. {Fin de condicional del paso 1}

### Código
```python
def inserta_cola(cola, max, frente, final, dato):
    if final < max:  
        final += 1  
        cola[final] = dato  # Inserta el DATO en la cola
        if final == 1:  
            frente = 1 
    else:
        print("Desbordamiento - Cola llena")
```
***
# Algoritmo 3.8

## Elimina_cola (COLA, FRENTE, FINAL, DATO)

### Descripción
Este algoritmo elimina el primer elemento de una estructura tipo cola y lo almacena en `DATO`. `FRENTE` y `FINAL` son los punteros que indican, respectivamente, el inicio y fin de la cola.

### Algoritmo
1. Si (`FRENTE != 0`) {Verifica que la cola no esté vacía}
   - *entonces*
     - Hacer `DATO <- COLA[FRENTE]` 
     - 1.1 Si (`FRENTE = FINAL`) {Si hay un solo elemento}
       - *entonces*
         - Hacer `FRENTE <- 0` y `FINAL <- 0` {Indica `COLA` vacía}
       - *si no*
         - Hacer `FRENTE <- FRENTE + 1`
     - 1.2 {Fin del condicional del paso 1.1}
   - *si no*
     - Escribir "Subdesbordamiento - Cola vacía"
2. {Fin de condicional del paso 1}

### Código
```python
def elimina_cola(cola, frente, final, dato):
    if frente != 0:  
        dato = cola[frente]  
        if frente == final:  
            frente = 0  
            final = 0
        else:
            frente += 1  
    else:
        print("Subdesbordamiento - Cola vacía")

```
***
# Algoritmo 3.9

## Cola_vacia (COLA, FRENTE, BAND)

### Descripción
Este algoritmo determina si una estructura de datos tipo cola está vacía, asignando a `BAND` el valor de verdad correspondiente.

### Algoritmo
1. Si (`FRENTE = 0`) 
   - *entonces*
     - Hacer `BAND <- VERDADERO` 
   - *si no*
     - Hacer `BAND <- FALSO`
2. {Fin de condicional del paso 1}

### Código
```python
def cola_vacia(cola, frente, band):
    if frente == 0:  
        band = True 
    else:
        band = False  
```
***
# Algoritmo 3.10

## Cola_llena (COLA, FINAL, MAX, BAND)

### Descripción
Este algoritmo determina si una estructura de datos tipo cola está llena, asignando a `BAND` el valor de verdad correspondiente. `MAX` es el número máximo de elementos que puede almacenar `COLA`.

### Algoritmo
1. Si (`FINAL = MAX`) 
   - *entonces*
     - Hacer `BAND <- VERDADERO` 
   - *si no*
     - Hacer `BAND <- FALSO`
2. {Fin de condicional del paso 1}

### Código
```python
def cola_llena(cola, final, max, band):
    if final == max:  
        band = True  
    else:
        band = False 
```
***
# Algoritmo 3.11
## Inserta_circular (COLACIR, MAX, FRENTE, FINAL, DATO)
### Descripción
Este algoritmo inserta el elemento `DATO` al final de una estructura tipo cola circular `COLACIR`. `FRENTE` y `FINAL` son los punteros que indican, respectivamente, el inicio y el fin de la cola circular. `MAX` es el número máximo de elementos que puede almacenar `COLACIR`.

### Algoritmo
1. Si ((`FINAL = MAX`) y (`FRENTE = 1`)) o ((`FINAL + 1) = FRENTE`)
   - *entonces*
       - Escribir "Desbordamiento-Cola llena"
   - *si no* 
      - 1.1 Si (`FINAL = MAX`)  
        - *entonces*
          - Hacer `FINAL <- 1` 
        - *si no*
          - Hacer  `FINAL <- FINAL + 1`
      - 1.2 {Fin del condicional del paso 1.1}
        - Hacer `COLACIR[FINAL] <- DATO`
      - 1.3 Si (`FRENTE = 0`) *entonces*
        - Hacer `FRENTE <- 1`
      - 1.4 {Fin del condicional del paso 1.3}
2. {Fin de condicional del paso 1}

### Código
```python
def inserta_circular(colacir, max, frente, final, dato):
    if (final == max and frente == 1) or (final + 1 == frente): 
        print("Desbordamiento - Cola llena")
    else:
        if final == max:  
            final = 1  
        else:
            final += 1  
        colacir[final] = dato 
        if frente == 0:  
            frente = 1  

```
***
# Algoritmo 3.12
## Elimina_circular (COLACIR, MAX, FRENTE, FINAL, DATO)
### Descripción
Este algoritmo elimina el primer elemento de una estructura tipo cola circular `COLACIR` y lo almacena en `DATO`. `FRENTE` y `FINAL` son los punteros que indican, respectivamente, el inicio y el fin de la estructura. `MAX` es el tamaño de `COLACIR`.

### Algoritmo
1. Si (`FRENTE = 0`) {Verifica si la cola está vacía}
   - *entonces*
       - Escribir "Subdesbordamiento-Cola vacía"
   - *si no*
       - Hacer `DATO <- COLACIR [FRENTE]`
      - 1.1 Si (`FRENTE = FINAL`) {Si hay sólo un elemento}
        - *entonces*
          - Hacer `FRENTE <- 0` y  `FINAL <- 0`
        - *si no*
        - 1.1.1 Si (`FRENTE = MAX`)
          - *entonces*
            - Hacer `FRENTE <- 1`
          - *si no*
            - Hacer `FRENTE <- FRENTE + 1`
        - 1.1.2 {Fin del condicional 1.1.1}
      - 1.4 {Fin del condicional del paso 1.1}
2. {Fin de condicional del paso 1}

### Código
```python
def elimina_circular(colacir, max, frente, final, dato):
    if frente == 0:  
        print("Subdesbordamiento - Cola vacía")
    else:
        dato = colacir[frente]  
        if frente == final:  
            frente = 0  
            final = 0
        else:
            if frente == max:  
                frente = 1 
            else:
                frente += 1 
```
***
# Ejemplo 3.7

En la figura 3.18a se presenta una estructura tipo cola circular de máximo 8 elementos `(MAX=8)`, en la cual ya se han almacenado algunos valores. 


Si se quisiera insertar otro elemento se presentaría un error de desbordamiento, ya que `FINAL + 1 = FRENTE`. 

A continuación se eliminan los valores `XX, YY, ZZ, KK, y VV` en ese orden.



Ahora se elimina el siguiente elemento `RR`. Al ser `FRENTE = MAX`, se le da el valor de 1.



Al eliminar `NN`, como `FRENTE = FINAL`, es decir, sólo quedaba un elemento en la cola, actualizamos los dos punteros en cero. La cola queda vacía.
