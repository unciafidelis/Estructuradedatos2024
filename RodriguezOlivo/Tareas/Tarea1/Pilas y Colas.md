
Juana Guadalupe Rodriguez Olivo
## Pilas

### Algoritmos básicos para pilas
````
Algoritmo Pila_vacia(PILA, TOPE, BAND)

  Si (TOPE = 0)

    BAND <- VERDADERO

  Si no

    BAND <- FALSO

  

Algoritmo Pila_llena(PILA, TOPE, MAX, BAND)  

  Si (TOPE = MAX)

    BAND <- VERDADERO

  Si no

    BAND <- FALSO

  

Algoritmo Pone(PILA, TOPE, MAX, DATO)

  Si (TOPE < MAX)

    TOPE <- TOPE + 1

    PILA[TOPE] <- DATO

  Si no

    Escribir "Desbordamiento - Pila llena"

  

Algoritmo Quita(PILA, TOPE, DATO)

  Si (TOPE > 0)

    DATO <- PILA[TOPE]

    TOPE <- TOPE - 1

  Si no

    Escribir "Subdesbordamiento - Pila vacía"
   ````

#### Ejemplos de uso de pilas

##### Ejemplo 3.1: Inserción y eliminación en una pila
````
Insertar: lunes, martes, miércoles, jueves, viernes

Eliminar: viernes

Ejemplo 3.2: Conversión de notación infija a postfija

CopyInfija: X + Z * W

Postfija: X Z W * +

  

Infija: (X + 2) * W / T ^ Y - V  

Postfija: X 2 + W * T Y ^ / V -
````
##### Algoritmo de conversión de infija a postfija

````Algoritmo Conv_postfija(EI, EPOS)

  TOPE <- 0

  Mientras (EI no sea vacía) hacer

    Tomar símbolo más a la izquierda de EI

    Si (es paréntesis izquierdo)

      Poner en PILA

    Si no, si (es paréntesis derecho)

      Mientras (PILA[TOPE] != paréntesis izquierdo) hacer

        Quitar de PILA y agregar a EPOS

      Quitar paréntesis izquierdo de PILA

    Si no, si (es operando)  

      Agregar a EPOS

    Si no

      Mientras (prioridad <= PILA[TOPE]) hacer

        Quitar de PILA y agregar a EPOS

      Poner símbolo en PILA

  Vaciar PILA en EPOS
  ````

##### Algoritmo de conversión de infija a prefija

````Algoritmo Conv_prefija(EI, EPRE)

  TOPE <- 0

  Mientras (EI no sea vacía) hacer

    Tomar símbolo más a la derecha de EI

    Si (es paréntesis derecho)

      Poner en PILA

    Si no, si (es paréntesis izquierdo)

      Mientras (PILA[TOPE] != paréntesis derecho) hacer

        Quitar de PILA y agregar a EPRE

      Quitar paréntesis derecho de PILA

    Si no, si (es operando)

      Agregar a EPRE

    Si no

      Mientras (prioridad < PILA[TOPE]) hacer

        Quitar de PILA y agregar a EPRE

      Poner símbolo en PILA

  Vaciar PILA en EPRE

  Invertir EPRE

Colas
````

### Algoritmos básicos para colas

````Algoritmo Inserta_cola(COLA, MAX, FRENTE, FINAL, DATO)

  Si (FINAL < MAX)

    FINAL <- FINAL + 1

    COLA[FINAL] <- DATO

    Si (FINAL = 1)

      FRENTE <- 1

  Si no

    Escribir "Desbordamiento - Cola llena"
````
  

##### Algoritmo Elimina_cola(COLA, FRENTE, FINAL, DATO)
````
  Si (FRENTE != 0)

    DATO <- COLA[FRENTE]

    Si (FRENTE = FINAL)

      FRENTE <- 0

      FINAL <- 0

    Si no

      FRENTE <- FRENTE + 1

  Si no

    Escribir "Subdesbordamiento - Cola vacía"
````
  

##### Algoritmo Cola_vacia(COLA, FRENTE, BAND)
````
  Si (FRENTE = 0)

    BAND <- VERDADERO

  Si no

    BAND <- FALSO
````
  

##### Algoritmo Cola_llena(COLA, FINAL, MAX, BAND)
````
  Si (FINAL = MAX)

    BAND <- VERDADERO

  Si no

    BAND <- FALSO
````
#### Ejemplo de uso de colas

##### Ejemplo 3.6: Inserción en una cola
````
Insertar: lunes, martes, miércoles, jueves, viernes
````