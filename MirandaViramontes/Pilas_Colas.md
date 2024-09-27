# Algoritmo 3.1
## Pila_vacia (PILA, TOPE, BAND)

### Descripción
Este algoritmo verifica si una estructura tipo pila `PILA` está vacía, asignando a `BAND`
el valor de verdad correspondiente. La pila se implementa en un arreglo unidimensional. `TOPE` 
es un parámetro de tipo entero. `BAND` es un parámetro de tipo booleano.

### Algoritmo
1. Si (`TOPE=0`) {Verifica si no hay elementos almacenados en la pila}
     - entonces
         - Hacer `BAND <- VERDADERO` {La pila está vacía}
     - si no
         - Hacer `BAND <- FALSO` {La pila no está vacía}
  2. {Fin del condicional del paso 1}

### Código

# Algoritmo 3.2
## Pila_llena (PILA, TOPE, MAX, BAND)
### Descripción
 Este algoritmo verifica si una estructura tipo pila `PILA` está llena, asignando a `BAND` el 
 valor de verdad correspondiente. La pila se implementa en un arreglo unidimensional de `MAX`
 elementos. `TOPE` es un parámetro de tipo entero. `BAND` es un parámetro de tipo boooleano.
 ### Algoritmo
  1. Si (`TOPE=MAX`) 
     - entonces
         - Hacer `BAND <- VERDADDERO` {La pila está llena}
     - si no
         - Hacer `BAND <- FALSO` {La pila no está llena}
  2. {Fin del condicional del paso 1}
### Código

# Algoritmo 3.3
## Pone (PILA, TOPE, MAX, DATO)
### Descripción
Este algoritmo agrega el elemento `DATO` en una estructura tipo pila `PILA`, si la misma
 no está llena. Actualiza el valor de `TOPE`. `MAX` representa el número máximo de elementos
 que puede almacenar `PILA`. `TOPE` es un parámetro de tipo entero.
 ### Algoritmo
  1. Llamar a `Pila_llena` con `PILA`, `TOPE`, `MAX` y `BAND`
  2. Si (`BAND=VERDADERO`)
      - entonces
          - Escribir "Desbordamiento-Pila llena"
      - si no
          - Hacer `TOPE <- TOPE + 1` y `PILA[TOPE] <- DATO`
          {Actualiza TOPE e inserta el nuevo elemento en el TOPE de PILA}
  3. {Fin de condicional del paso 2}
### Código

# Algoritmo 3.4
## Quita (PILA, TOPE, DATO)
### Descripción
Este algoritmo saca un elemento `DATO` de unaestructura tipo pila `PILA`, si ésta n
 se encuentra vacía. El elemento que se elimina es el que se encuentra en la posición indicada
 por `TOPE`.
 ### Algoritmo
  1. Llamar a `Pila_vacia` con `PILA`, `TOPE` y `BAND`
  2. Si (`BAND=VERDADERO`)
      - entonces
          - Escribir "Subdesbordamiento-Pila vacía"
      - si no
          - Hacer `DATO <- PILA[TOPE]` y `TOPE <- TOPE - 1` {Actualiza TOPE}
  3. {Fin de condicional del paso 2}
### Código


# Ejemplo 3.1
# Ejemplo 3.2

# Algoritmo 3.5
## Conv_postfija (EL, EPOS)
### Descripción
Este algoritmo traduce una expresión infija (EI) a postfija (EPOS), haciendo uso de 
una pila (PILA). MAX es el número máximo de elementos que puede almacenar la pila.

### Algoritmo
1. Hacer `TOPE <- 0`
2. Mientras (`EL` sea diferente de la cadena vacía) Repetir
   - Tomar el símbolo más a la izquierda de `EL`. Recortar luego la expresión.
   - 2.1 Si (el símbolo es paréntesis izquierdo):
       - Entonces `Poner símbolo en PILA`. Se asume que hay espacio en `PILA`
         - Llamar a `Pone` con `PILA`, `TOPE`, `MAX` y símbolo
       - sino
      - 2.1.1 Si (el símbolo es paréntesis derecho):
           - Entonces
              - 2.1.1.1 Mientras (`PILA[TOPE] != paréntesis izquierdo`) Repetir
                - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
                - Hacer `EPOS <- EPOS + DATO`
             - 2.1.1.2 {Fin del ciclo del paso 2.1.1.1}
               - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
                {Se quita el paréntesis izquierdo de `PILA` y no se agrega a `EPOS`}
                - sino
             - 2.1.1.3 Si (el símbolo es un operador):
               - Entonces:
                 - Agregar símbolo a `EPOS`
               - si no {Es un operador}
               - Llamar `Pila_vacia` con `PILA`, `TOPE` y `BAND`
                - 2.1.1.3A Mientras (`BAND = FALSO`) y (la prioridad del operador sea <= que la prioridad del operador que está encima de `PILA`) Repetir
                   - Llamar a `Quita` con `PILA`, `TOPE`, `DATO`
                   - Hacer `EPOS <- EPOS + DATO`
                   - Llamar a `Pila_vacia` con `PILA`, `TOPE` y `BAND`
               - 2.1.1.3B {Fin del ciclo del paso 2.1.1.3A}
                   - Llamar a `Pone` con `PILA`, `TOPE` y simbolo
              - 2.1.1.4 {Fin del condicional del paso 2.1.1.3}:
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

### Código

# Ejemplo 3.3
# Ejemplo 3.4

# Algoritmo 3.6
## Conv_pretfija (EL, EPRE)
### Descripción
 Este algoritmo traduce una expresión en notación infija, (El) a prefija, (EPRE), haciendo uso de
 una pila (PILA)
 (TOPE) es una variable de tipo entero y (MAX) representa el máximo número de elementos que
 puede almacenar la pila}

### Algoritmo
1. Hacer `TOPE <- 0`
2. Mientras (`EL` sea diferente de la cadena vacía) Repetir
   - Tomar el símbolo más a la derecha de `EL` recortartando luego la expresión
   - 2.1 Si (el símbolo es paréntesis derecho)
       - Entonces {Poner símbolo en pila} 
         - Llamar a `Pone` con `PILA`, `TOPE`, `MAX` y símbolo
       - sino
      - 2.1.1 Si (el símbolo es paréntesis izquierdo):
           - Entonces
              - 2.1.1.1 Mientras (`PILA[TOPE] != paréntesis derecho`) Repetir
                - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
                - Hacer `EPRE <- EPORE + DATO`
             - 2.1.1.2 {Fin del ciclo del paso 2.1.1.1}  {Sacamos el paréntesis derecho de PILA y no se agrega a EPRE}
               - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
              - sino
             - 2.1.1.3 Si (el símbolo es un operador):
               - Entonces:
                 - Agregar símbolo a `EPRE`
               # FALTA PAGINA 90 Y 91
### Código

# Algoritmo 3.7
## Inserta_cola (COLA, MAX, FRENTE, FINAL, DATO)
### Descripción
Este algoritmo inserta el elemento `DATO` al final de una estructura tipo cola. `FRENTE` y `FINAL`
son los punteros que indican, respectivamente, el inicio y fin de `COLA`. La primera vez
 `FRENTE` y `FINAL` tienen el valor O, ya que la cola está vacía. `MAX` es el máximo número de
 elementos que puede almacenar la cola
 ### Algoritmo
  1. Si (`FINAL<MAX`) {Verifica que hay espacio libre}
     - entonces
       - Hacer `FINAL <- FINAL + 1` {Actualiza `FINAL`} y `COLA[FINAL] <- DATO`
      - 1.1 Si (`FINAL = 1`) entonces {Se insertó el primer elemento de `COLA`}
          - Hacer `FRENTE <- 1`
      - 1.2 {Fin del condicional del paso 1.1}
          - si no
            - Escribir "Desbordamiento-Cola llena"
  2. {Fin de condicional del paso 1}
### Código

# Algoritmo 3.8
## Elimina_cola (COLA, FRENTE, FINAL, DATO)
### Descripción
Este algoritmo eliminael primerelemento de una estructura tipo cola y lo almacenaen `DATO`.
 `FRENTE` y `FINAL` son los punteros que indican, respectivamente, el inicio y fin de la cola
 ### Algoritmo
  1. Si (`FRENTE != 0`) {Verifica que la cola no este vacía}
     - entonces
       - Hacer `DATO <- COLA [FRENTE]` 
        - 1.1 Si (`FRENTE = FINAL`)  {Si hay un solo elemento}
          - entonces
            - Hacer `FRENTE <- 0` y `FINAL <- 0` {Indica `COLA` vacía}
          - si no
            - Hacer  `FRENTE <- FRENTE + 1`
        - 1.2 {Fin del condicional del paso 1.1}
          - si no
            - Escribir "Subdesbordamiento-Cola vacía"
  2. {Fin de condicional del paso 1}
### Código

# Algoritmo 3.9
## Cola_vacia (COLA, FRENTE, BAND)
### Descripción
Este algoritmo determina si una estructura de datos tipo cola está vacía, asignando a `BAND`
 el valor de verdad correspondiente
 ### Algoritmo
  1. Si (`FRENTE = 0`) 
     - entonces
       - Hacer `BAND <- VERDADERO` 
     - si no
       - Hacer `BAND <- FALSO`
  2. {Fin de condicional del paso 1}
### Código

# Algoritmo 3.10
## Cola_llena (COLA, FINAL, MAX, BAND)
### Descripción
Este algoritmo determina si una estructura de datos tipo cola está llena, asignando a `BAND`
 el valor de verdad correspondiente. `MAX` es el número máximo de elementos que puede
 almacenar `COLA`
 ### Algoritmo
  1. Si (`FINAL = MAX`) 
     - entonces
       - Hacer `BAND <- VERDADERO` 
     - si no
       - Hacer `BAND <- FALSO`
  2. {Fin de condicional del paso 1}
### Código

# Ejemplo 3.6

# Algoritmo 3.11
## Inserta_circular (COLACIR, MAX, FRENTE, FINAL, DATO)
### Descripción
Este algoritmo inserta el elemento `DATO` al final de una estructura tipo cola circular `COLACIR`.
`FRENTE` y `FINAL` son los punteros que indican, respectivamente, el inicio y el fin de la cola circular.
`MAX` es el número máximo de elementos que puede almacenar `COLACIR`
 ### Algoritmo
  1. Si ((`FINAL = MAX`) y (`FRENTE = 1`)) o ((`FINAL + 1) = FRENTE`)
     - entonces
         - Escribir "Desbordamiento-Cola llena"
     - sino 
        - 1.1 Si (`FINAL = MAX`)  
          - entonces
            - Hacer `FINAL <- 1` 
          - si no
            - Hacer  `FINAL <- FINAL + 1`
        - 1.2 {Fin del condicional del paso 1.1}
          - Hacer `COLACIR[FINAL] <- DATO`
        - 1.3 Si (`FRENTE = 0`) entonces
          - Hacer `FRENTE <- 1`
        - 1.4 {Fin del condicional del paso 1.3}
  2. {Fin de condicional del paso 1}
### Código

# Algoritmo 3.12
## Elimina_circular (COLACIR, MAX, FRENTE, FINAL, DATO)
### Descripción
Este algoritmo elimina el primer elemento de una estructura tipo cola circular `COLACIR`y lo alamacena en `DATO` 
`FRENTE` y `FINAL` son los punteros que indican, respectivamente, el inicio y el fin de la estructura.
`MAX` es el tamaño de `COLACIR`
 ### Algoritmo
  1. Si (`FRENTE = 0`) {Verifica si la cola está vacía}
     - entonces
         - Escribir "Subdesbordamiento-Cola vacía"
     - sino
         - Hacer `DATO <- COLACIR [FRENTE]`
        - 1.1 Si (`FRENTE = FINAL`) {Si hay sólo un elemento}
          - entonces
            - Hacer `FRENTE <- 0` y  `FINAL <- 0`
          - si no
          - 1.1.1 Si (`FRENTE = MAX`)
            - entonces
              - Hacer `FRENTE <- 1`
            - si no
              - Hacer `FRENTE <- FRENTE + 1`
          - 1.1.2 {Fin del condicional 1.1.1}
        - 1.4 {Fin del condicional del paso 1.1}
  2. {Fin de condicional del paso 1}
### Código

# Ejemplo 3.7
