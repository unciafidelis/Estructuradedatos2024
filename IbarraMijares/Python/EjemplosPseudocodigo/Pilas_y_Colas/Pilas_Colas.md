# DAVID IBARRA MIJARES

# CAPÍTULO 3 - PILAS Y COLAS

### 3.1 INTRODUCCIÓN
Este capítulo se dedica al estudio de pilas y colas, que son estructuras de datos lineales con restricciones en cuanto a la posición en la cual se pueden llevar a cabo las operaciones de inserción y eliminación de componentes.

### 3.2 PILAS
Una pila representa una estructura lineal de datos en la que se puede agregar o quitar elementos únicamente por uno de los dos extremos. En consecuencia, los elementos de una pila se eliminan en orden inverso al que se insertaron; es decir, el último elemento que se mete en la pila es el primero que se saca. Debido a esta característica, se le conoce como estructura LIFO Last-Input, First-Output.

#### Algoritmo 3.1: Pilas_Vacía

1. Si (TOPE =O) (Verifica si no hay elementos almacenados en la pila)
        entonces
            Hacer BAND <- VERDADERO (La pila está vacía)
        si no
            Hacer BAND <- FALSO (La pila no está vacía)
2. (Fin del condicional del paso 1)

- Código: 
```py
def Pilas_Vacía (tope, band):
if tope == 0:
    band = True
else: 
    band = False
```

#### Algoritmo 3.2: Pila_llena

1. Si (TOPE =MAX)
    entonces
        Hacer BAND <- VERDADERO (La pila está llena)
    si no
        Hacer BAND <- FALSO (La pila no está llena)
2. (Fin del condicional del paso 1)

- Código
```py
def pila_llena(tope, band, max)
if tope == max:
    band = True
else:
    band = False
```


#### Algoritmo 3.3: Pone
    
1. Llamar a Pila_llena con PILA, TOPE, MAX Y BAND
2. Si (BAND = VERDADERO)
    entonces
        Escribir "Desbordamiento - Pila llena"
    si no
        Hacer TOPE <- TOPE + 1 y PILA[TOPE] <- DATO
        (Actualiza TOPE e inserta el nuevo elemento en el TOPE de PILA)

3. (Fin del condicional del paso 2)

- Código: 
```py
def pone(pila, tope, max, dato):
if band == True:
    print("Desbordamiento - Pila llena)
else:
    tope = tope + 1
    pila[tope] = dato
```


#### Algoritmo 3.4: Quita
1. Llamar a Pila_vacía con PILA, TOPE Y BAND
2. Si (BAND = VERDADERO)
    entonces
        Escribir "Subdesbordarniento - Pila vacía"
    si no
        Hacer DATO <- PILA [TOPE] Y TOPE <- TOPE - 1 {Actualiza TOPE}
3. (Fin del condicional del paso 2)

- Código
```py
def quita(pila,tope,band):
    pila_vacia(pila,tope,band)

    if band == True:
        print("Subdesbordamiento - Pila Vacía")
    else:
        dato = pila[tope]
        tope = tope - 1
```
### Ejemplo 3.1
Si se insertaran los elementos lunes, martes, miércoles, jueves y viernes en PILA, la estructura quedaría tal y como se muestra en la figura 3.6a.
Ahora bien, si se eliminará el elemento viernes, el TOPE apuntaría ahora a jueves (fig. 3.6b).

![alt text](<3.6.png>)
*Figura 3.6*

Una forma de resolver este problema es eliminar primeramente los elementos jueves y miércoles, de esta manera martes quedaría ubicado en la cima de PILA y ahora sería posible extraerlo (figuras 3.7a, 3.7b y 3.7c).

### 3.2.3 Aplicacion de pilas

Las pilas son una estructura de datos muy usada en la solución de diversos tipos de problemas, en el área de la computación. Ahora se analizarán algunos de los casos más representativos de aplicación de las mismas:

![alt text](<3.7.png>)
*Figura 3.7*

### Ejemplo 3.2

En este ejemplo se exponen dos casos de traducción de notación infija a posfija. El primero de ellos es una expresión simple, mientras que el segundo presenta mayor grado de complejidad. En la tabla 3.1 se muestran los pasos necesarios para lograr la traducción de la primera expresión, yen la tabla 3.2 los correspondientes a la segunda expresión:

**Expresión infija: X+Z*W**
**Expresión posfija: XZW*+**

El primer operador que se procesa durante la traducción de la expresión es la multiplicación, paso 1, debido a que es el de más alta prioridad. 
Se coloca el operador de tal manera que los operandos afectados por él lo precedan. Para el operador de suma se sigue el mismo criterio, los dos operandos lo preceden. En este caso el primer operando es X y el segundo es ZW*.

![alt text](<3.1.png>)
*tabla 3.1*

***Expresión infija: (X+Z)*W/T^Y-V ***

***Expresión postfija: XZ+W*TY^/V- ***

![alt text](<3.2.png>)
*Tabla 3.2*

En el paso 1 se convierte la subexpresión que se encuentra entre paréntesis por ser la de más alta prioridad. Luego se sigue con el operador de potencia, paso 2, y así con los demás, según su jerarquía. Como consecuencia de que la multiplicación y la división tienen igual prioridad, se procesa primero la multiplicación por encontrarse más a la izquierda en la expresión, paso 3. El operador de la resta es el último que se mueve, paso 5. A continuación se presenta el algoritmo que traduce una expresión infija a otra posfija.

#### Algoritmo 3.5 Conv_Postfija

Este algoritmo traduce una expresión infija -El- a postfija -EPOS-, haciendo uso de una pila -PILA-. MAX es el número máximo de elementos que puede almacenar la pila

1. Hacer `TOPE <- 0`
2. Mientras (`EL` sea diferente de la cadena vacía) Repetir
   - Tomar el símbolo más a la izquierda de `EL`. Recortar luego la expresión.
   - 2.1 Si (el símbolo es paréntesis izquierdo):
       - *entonces* (Poner símbolo en `PILA`. Se asume que hay espacio en `PILA`)
         - Llamar a `Pone` con `PILA`, `TOPE`, `MAX` y símbolo
       - *sino*
      - 2.1.1 Si (el símbolo es paréntesis derecho):
           - *entonces*
              - 2.1.1.1 Mientras (`PILA[TOPE] != paréntesis izquierdo`) Repetir
                - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
                - Hacer `EPOS <- EPOS + DATO`
             - 2.1.1.2 {Fin del ciclo del paso 2.1.1.1}
               - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
                (Se quita el paréntesis izquierdo de `PILA` y no se agrega a `EPOS`)
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
              - 2.1.1.4 {Fin del condicional del paso 2.1.1.3}:
      - 2.1.2 {Fin del condicional del paso 2.1.1}
    - 2.2 {Fin del condicional del paso 2.1}
3. {Fin del ciclo del paso 2}
4. Llamar `Pila_vacia` con `PILA`, `TOPE` y `BAND`
5. Mientras (`BAND = FALSO`) Repetir:
   - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
   - Hacer `EPOS <- EPOS + DATO`
   - Llamar a `Pila_vacia` con `PILA`, `TOPE` y `BAND`
6. (Fin del ciclo del paso 5)
7. Escribe `EPOS`

- Código
```python
def infija_a_postfija(EL,EPOS):
    while EL:
        simbolo = EL[0]  
        EL = EL[1:]      
        if simbolo == '(': 
            TOPE = pone(PILA, TOPE, simbolo)
        elif simbolo == ')': 
            while PILA[TOPE-1] != '(': 
                TOPE, DATO = quita(PILA, TOPE)
                EPOS += DATO
            TOPE, _ = quita(PILA, TOPE) 
        elif es_operador(simbolo):  
            while not pila_vacia(PILA, TOPE) and prioridad(simbolo) <= prioridad(PILA[TOPE-1]):
                TOPE, DATO = quita(PILA, TOPE)
                EPOS += DATO
            TOPE = pone(PILA, TOPE, simbolo)
        else: 
            EPOS += simbolo
    while not pila_vacia(PILA, TOPE):
        TOPE, DATO = quita(PILA, TOPE)
        EPOS += DATO
    return EPOS

```

### Ejemplo 3.3

En este ejemplo se retoman los casos del ejemplo 3.2 para ilustrar el funcionamiento del algoritmo Conv_posfija.

***Expresión infija: X+Z*W ***
***Expresión posfija: XZW*+ ***


![alt text](<3.3.png>)
*Tabla 3.3*
En la tabla 3.3 se presentan los pasos necesarios para lograr la traducción deseada siguiendo el algoritmo 3.5.En los pasos 1, 3 y 5 el símbolo analizado -un operando- se agrega directamente a EPOS. Al analizar el operador +, paso 2, se verifica si en PILA hay operadores con mayor o igual prioridad. En este caso, PILA está vacía, por tanto, se pone el símbolo en el tope de ella. Con el operador *, paso 4, sucede algo similar. En PILA no existen operadores de mayor o igual prioridad -la suma tiene menor prioridad que la multiplicación-, por lo que se agrega el operador * a PILA. En los dos últimos pasos, 6 y 7, se extraen de PILA sus elementos, agregándolos a EPOS.

***Expresión infija: (X + 2) * W / T 1\ Y - V***
***Expresión postfija: XZ+W * TYI\N- ***

En la tabla 3.4 se presentan los pasos necesarios para lograr la traducción deseada, siguiendo el algoritmo 3.5.

### Ejemplo 3.4

En este ejemplo se exponen dos casos de traducción de notación infija a prefija. El primero de ellos es una expresión simple, mientras que el segundo presenta mayor grado de complejidad.

***Expresión infija: X + Z * W ***
***Expresión prefija: + X*ZW ***

![alt text](<3.4.png>)
*Tabla 3.4*

En la tabla 3.5 se presentan los pasos necesarios para lograr la traducción deseada.Como en el caso de la notación postfija, ejemplo 3.2, aquí también el operador de multiplicación se procesa primero. De la traducción de la expresión, paso 1, resulta el operador precediendo a los operandos. Lo mismo para el operador de suma, paso 2.

***Expresión infija: (X + Z)*W/T^Y-V ***
***Expresión prefija: -/*+XZW^TYV ***


![alt text](<3.5.png>)
*Tabla 3.5*

![alt text](<3.6.png>)
*Tabla 3.6*

En la tabla 3.6 se presentan los pasos necesarios para lograr la traducción deseada. Lo primero que se procesa en este caso es la subexpresión que se encuentra entre el paréntesis, paso 1.

El orden en que se procesan los operadores es el mismo que se siguió para la conversión de infija a posfija. Por tanto, sería reiterativo volver a explicar paso a paso el contenido de la tabla 3.6. Sin embargo, es de destacar la posición que ocupan los operadores con respecto a los operandos: los primeros preceden a los segundos.

A continuación se incluye el algoritmo de conversión de notación infija a prefija. Este algoritmo se diferencia del anterior básicamente en el hecho de que los elementos de la expresión en notación infija se recorrerán de derecha a izquierda.

#### Algoritmo 3.6: Conv_prefija

1. Hacer `TOPE <- 0`
2. Mientras (`EL` sea diferente de la cadena vacía) Repetir
   - Tomar el símbolo más a la derecha de `EL` recortartando luego la expresión
   - 2.1 Si (el símbolo es paréntesis derecho)
       - *entonces* {Poner símbolo en pila} 
         - Llamar a `Pone` con `PILA`, `TOPE`, `MAX` y símbolo
       - *si no*
      - 2.1.1 Si (el símbolo es paréntesis izquierdo):
           - *entonces*
              - 2.1.1.1 Mientras (`PILA[TOPE] != paréntesis derecho`) Repetir
                - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
                - Hacer `EPRE <- EPORE + DATO`
             - 2.1.1.2 {Fin del ciclo del paso 2.1.1.1}  {Sacamos el paréntesis derecho de PILA y no se agrega a EPRE}
               - Llamar a `Quita` con `PILA`, `TOPE` y `DATO`
              - *si no*
             - 2.1.1.3 Si (el símbolo es un operador):
               - *entonces*
                 - Agregar símbolo a `EPRE`
               # FALTA PÁGINA 90 Y 91

### Clase Pila

La clase Pila tiene atributos y métodos. Los atributos son la colección de elementosel TOPE. Los métodos, por otra parte, son todas aquellas operaciones analizadas en la sección anterior -Pila_vacía, Pila_llena, Pone y Quita-. 

![alt text](<3.10.png>)
*Figura 3.10*

### 3.3 COLAS

Una cola constituye una estructura lineal de datos en la que los nuevos elementos se introducen por un extremo y los ya existentes se eliminan por el otro. Es importante señalar que los componentes de la cola se eliminan en el mismo orden en el cual se insertaron. 

Es decir, el primer elemento que se introduce en la estructura será el que se eliminará en primer orden. Debido a esta característica, las colas también reciben el nombre de estructuras FIFO (First-In, First-Out: el primero en entrar es el primero en salir).

### 3.3.1 Representación de Colas

Las colas, al igual que las pilas, no existen como estructuras de datos estándar en los lenguajes de programación. Este tipo de estructura de datos se puede representar mediante el uso de:

- Arreglos
- Listas

![alt text](<3.12.png>)
*Figura 3.12*

![alt text](<3.13.png>)
*Figura 3.13*

En la figura 3.13, por otra parte, se presentan ejemplos de: a) cola llena, b) cola con algunos elementos y c) cola vacía.

### 3.3.2 Operaciones con Colas

La definición de la estructura de datos tipo cola queda completa al incluir las operaciones que se pueden realizar en ella. Las operaciones básicas que pueden efectuarse son:

- Insertar un elemento en la cola
- Eliminar un elemento de la cola

Las inserciones se llevarán a cabo por el FINAL de la cola, mientras que las eliminaciones se harán por el FRENTE recuerde que el primero en entrar es el primero en salir.

Considerando que una cola puede almacenar un máximo número de elementos y que además FRENTE indica la posición del primer elemento y FINAL la posición del último, se presentan a continuación los algoritmos correspondientes a las operaciones mencionadas.


 
#### Algoritmo 3.7   Inserta_cola

Este algoritmo inserta el elemento `DATO` al final de una estructura tipo cola. `FRENTE` y `FINAL` son los punteros que indican, respectivamente, el inicio y fin de `COLA`. La primera vez `FRENTE` y `FINAL` tienen el valor O, ya que la cola está vacía. `MAX` es el máximo número de elementos que puede almacenar la cola.

  1. Si (`FINAL<MAX`) {Verifica que hay espacio libre}
        entonces
             Hacer `FINAL <- FINAL + 1` {Actualiza `FINAL`} y `COLA[FINAL] <- DATO`
    1.1 Si (`FINAL = 1`) *entonces* {Se insertó el primer elemento de `COLA`}
             Hacer `FRENTE <- 1`
    1.2 {Fin del condicional del paso 1.1}
        si no
        Escribir "Desbordamiento-Cola llena"
  2. {Fin de condicional del paso 1}

- Código
```python
def inserta_cola(final, max, cola, frente):
    if final < max:  
        final = final + 1  
        cola[final] = dato  
        if final == 1:  
            frente = 1 
    else:
        print("Desbordamiento - Cola llena")
```

#### Algoritmo 3.8: Eliminar_Cola

Este algoritmo elimina el primer elemento de una estructura tipo cola y lo almacena en DATO. FRENTE y FINAL son los punteros que indican, respectivamente, el inicio y fin de la cola.

1. Si (`FRENTE != 0`) {Verifica que la cola no este vacía}
    entonces
        Hacer `DATO <- COLA [FRENTE]` 
    1.1. Si (`FRENTE = FINAL`)  {Si hay un solo elemento}
           entonces
                Hacer `FRENTE <- 0` y `FINAL <- 0` {Indica `COLA` vacía}
           si no
                Hacer  `FRENTE <- FRENTE + 1`
    1.2. {Fin del condicional del paso 1.1}
           si no
    Escribir "Subdesbordamiento-Cola vacía"
  2. {Fin de condicional del paso 1}

- Código
```py
def elimina_cola(cola, frente, final, dato):
    if frente != 0:  
        dato = cola[frente]  
        if frente == final:  
            frente = 0  
            final = 0
        else:
            frente = frente +  1  
    else:
        print("Subdesbordamiento - Cola vacía")
```

A continuación se presentan los algoritmos que permiten verificar el estado de una cola, quedando como tarea sugerida la reescritura de los dos algoritmos anteriores.

#### Algoritmo 3.9: Cola_Vacia

Este algoritmo determina si una estructura de datos tipo cola está vacía, asignando a BAND el valor de verdad correspondiente.
 
  1. Si (`FRENTE = 0`) 
    entonces
        Hacer `BAND <- VERDADERO` 
    si no
        Hacer `BAND <- FALSO`
  2. {Fin de condicional del paso 1}

- Código
```py
def cola_vacia(cola, frente, band):
    if frente == 0:  
        band = True 
    else:
        band = False  
```

#### Algoritmo 3.10: Cola_llena

Este algoritmo determina si una estructura de datos tipo cola está llena, asignando a BAND el valor de verdad correspondiente. `MAX` es el número máximo de elementos que puede almacenar `COLA`.
 
1. Si (`FINAL = MAX`) 
    entonces
        Hacer `BAND <- VERDADERO` 
    si no
        Hacer `BAND <- FALSO`
2. {Fin de condicional del paso 1}
     
- Código
```python
def cola_llena(cola, final, max, band):
    if final == max:  
        band = True  
    else:
        band = False 
```

### Ejemplo 3.6

Aquí se incluye un ejemplo para ilustrar el funcionamiento de las operaciones de inserción y eliminación en colas.

Retome el ejemplo 3.1 de la sección 3.1.2. Se insertan en COLA los elementos: lunes, martes, miércoles, jueves y viernes -en ese orden-, de modo que la estructura queda como se muestra en la figura 3.14. Para este ejemplo MAX =7.

![alt text](<3.14.png>)
*Figura 3.14*

![alt text](<3.15.png>)
*Figura 3.15*

El elemento lunes es el primero que se puede eliminar por el el primero que se insertó en la cola. Luego de la eliminación, `FRENTE` guarda la posición del suiguiente elemento (fig 3.15a). 

![alt text](<3.16.png>)
*Figura 3.16*

### 3.3.3 Colas Circulares

Una cola circular, constituye una estructura de datos lineal en la cual el siguiente elemento del útlimo en realidad es el primero.

![alt text](<3.17.png>)
*Figura 3.17*

#### Algoritmo 3.11: Inserta_circular

1. Si ((`FINAL = MAX`) y (`FRENTE = 1`)) o ((`FINAL + 1) = FRENTE`))
        entonces
            Escribir "Desbordamiento - Cola llena"
        si no
    1.1 Si (`FINAL = MAX`)  
        entonces
            Hacer `FINAL <- 1` 
        si no
            Hacer  `FINAL <- FINAL + 1`
    1.2 {Fin del condicional del paso 1.1}
            Hacer `COLACIR[FINAL] <- DATO`
    1.3 Si (`FRENTE = 0`) entonces
            Hacer `FRENTE <- 1`
    1.4 {Fin del condicional del paso 1.3}
2. {Fin de condicional del paso 1}
     
- Código
```python
def inserta_circular(final, max, frente, colacir, dato):
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
#### Algoritmo 3.12: Elimina_circular

1. Si (`FRENTE = 0`) {Verifica si la cola está vacía}
    entonces
        Escribir "Subdesbordamiento-Cola vacía"
    si no
        Hacer `DATO <- COLACIR [FRENTE]`
    1.1 Si (`FRENTE = FINAL`) {Si hay sólo un elemento}
        entonces
            Hacer `FRENTE <- 0` y  `FINAL <- 0`
        si no
    1.1.1 Si (`FRENTE = MAX`)
        entonces
            Hacer `FRENTE <- 1`
        si no
            Hacer `FRENTE <- FRENTE + 1`
     1.1.2 {Fin del condicional 1.1.1}
    1.4 {Fin del condicional del paso 1.1}
2. {Fin de condicional del paso 1}

- Código
```py
def elimina_circular(frente, dato, max, final, colacir):
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

### Ejemplo 3.7

A continuación se presenta un ejemplo para ilustrar el funcionamiento de las operaciones de inserción y elimnación en colas circulares.

En la figura 3.18a, se presenta una estrucutra tipo cola circular de máximo 8 elementos (MAX = 8), en la cual ya se han almacenado algunos valores. En la figura 3.18b se muestra el estado de la cola luego de insertar el elemento NN.

![alt text](<3.18.png>)
*Figura 3.18*

Si se quisiera insertar otro elemento se presentará un error de desbordamiento, ya que FINAL + 1 = FRENTE.
A continuación se eliminan los valores XX, YY, ZZ, KK ,TT y VV en ese orden. La cola queda como la figura 3.19

![alt text](<3.19.png>)
*Figura 3.19*

### 3.3.6 Clase Colas
La clase Cola tiene atributos y metodos, como cualquiera clase.

![alt text](<3.25.png>)
*Figura 3.25*