![[Pasted image 20241014153123.png]]

---

# **Capítulo 3: Pilas y Colas**

## **3.1 Introducción**

En este capítulo, nos enfocaremos en dos estructuras fundamentales de datos: **pilas** y **colas**. Estas estructuras lineales son usadas en problemas donde las operaciones se limitan a los extremos de la estructura.

- **Pilas**: Los datos solo se insertan y eliminan desde un extremo, el **tope**.
- **Colas**: Los datos se insertan en un extremo y se eliminan en el otro.

Ambas estructuras son cruciales para muchas aplicaciones en informática, como el manejo de recursividad, procesos y estructuras de control.

---

## **3.2 Pilas (LIFO - Last In, First Out)**

### **Definición de Pilas**

Una pila es una estructura de datos que sigue el principio de **Último en Entrar, Primero en Salir (LIFO)**. Los elementos solo pueden ser insertados y eliminados desde el **tope** de la pila, lo que significa que el último elemento en ser insertado será el primero en ser eliminado.

#### **Ejemplos Prácticos de Pilas**:
- **Pila de platos**: Imagina una pila de platos, donde solo puedes poner o quitar un plato desde la parte superior.
- **Retroceso en un navegador web**: Al navegar por distintas páginas, las visitas se apilan, y al retroceder, se elimina la última página que visitaste.

#### **Operaciones en Pilas**:
Las operaciones básicas que se pueden realizar sobre una pila incluyen:
1. **Pila_vacía**: Verifica si la pila está vacía.
2. **Pila_llena**: Verifica si la pila está llena.
3. **Pone (Push)**: Inserta un elemento en la pila.
4. **Quita (Pop)**: Elimina el elemento en el tope de la pila.

Estas operaciones se implementan con **arreglos** o **listas** y dependen de una variable **TOPE** que indica el índice del último elemento insertado.

### **Algoritmos para Pilas**

#### 1. **Pila_vacía**

El algoritmo **Pila_vacía** se utiliza para verificar si la pila está vacía, revisando si el valor de **TOPE** es igual a 0. Si es así, la pila está vacía.

```pseudo
Algoritmo Pila_vacía (PILA, TOPE, BAND)
   Si (TOPE == 0) Entonces
      BAND ← VERDADERO  // La pila está vacía
   Sino
      BAND ← FALSO      // La pila no está vacía
   Fin Si
Fin Algoritmo
```

#### **Explicación**:
- **Entrada**: El valor de **TOPE**, que indica el índice del último elemento insertado.
- **Salida**: El valor de **BAND** será verdadero si la pila está vacía, de lo contrario, será falso.

---

#### 2. **Pila_llena**

El algoritmo **Pila_llena** revisa si la pila ha alcanzado su tamaño máximo permitido, comparando el valor de **TOPE** con el tamaño máximo **MAX**.

```pseudo
Algoritmo Pila_llena (PILA, TOPE, MAX, BAND)
   Si (TOPE == MAX) Entonces
      BAND ← VERDADERO  // La pila está llena
   Sino
      BAND ← FALSO      // La pila no está llena
   Fin Si
Fin Algoritmo
```

#### **Explicación**:
- **Entrada**: El valor de **TOPE** y el tamaño máximo **MAX** de la pila.
- **Salida**: El valor de **BAND** será verdadero si la pila está llena, de lo contrario, será falso.

---

#### 3. **Pone (Push)**

El algoritmo **Pone** se utiliza para insertar un nuevo elemento en la pila. Antes de insertar el nuevo elemento, verifica si la pila está llena utilizando el algoritmo **Pila_llena**.

```pseudo
Algoritmo Pone (PILA, TOPE, MAX, DATO)
   Llamar a Pila_llena con (PILA, TOPE, MAX, BAND)
   Si (BAND == VERDADERO) Entonces
      Escribir "Desbordamiento - Pila llena"
   Sino
      TOPE ← TOPE + 1
      PILA[TOPE] ← DATO  // Inserta el nuevo dato en la pila
   Fin Si
Fin Algoritmo
```

#### **Explicación**:
- **Entrada**: El valor de **TOPE**, el tamaño máximo **MAX** y el **DATO** que se desea insertar.
- **Proceso**:
  1. Verifica si la pila está llena.
  2. Si no está llena, incrementa el valor de **TOPE** y almacena el nuevo dato en la posición correspondiente.
- **Salida**: La pila actualizada con el nuevo elemento insertado.

---

#### 4. **Quita (Pop)**

El algoritmo **Quita** se utiliza para eliminar el elemento en el tope de la pila. Si la pila está vacía, se reporta un **subdesbordamiento**.

```pseudo
Algoritmo Quita (PILA, TOPE, DATO)
   Llamar a Pila_vacía con (PILA, TOPE, BAND)
   Si (BAND == VERDADERO) Entonces
      Escribir "Subdesbordamiento - Pila vacía"
   Sino
      DATO ← PILA[TOPE]  // Obtiene el dato en el tope
      TOPE ← TOPE - 1    // Decrementa el tope
   Fin Si
Fin Algoritmo
```

#### **Explicación**:
- **Entrada**: El valor de **TOPE** y el arreglo **PILA**.
- **Proceso**:
  1. Verifica si la pila está vacía.
  2. Si no está vacía, elimina el elemento en el **tope** y decrece el valor de **TOPE**.
- **Salida**: El dato eliminado de la pila.

---

#### 5. **Conv_postfija (Conversión de infija a postfija)**

Este algoritmo convierte una expresión aritmética en notación **infija** (operadores entre operandos) a **notación postfija** (operadores después de los operandos) usando una pila.

```pseudo
Algoritmo Conv_postfija (EI, EPOS)
   Hacer TOPE ← 0
   Mientras (EI no sea cadena vacía) Repetir
      Tomar el símbolo más a la izquierda de EI
      Si (símbolo es un operando) Entonces
         Agregar símbolo a EPOS
      Si no Si (símbolo es un paréntesis izquierdo) Entonces
         Llamar a Pone con PILA y TOPE
      Si no Si (símbolo es un paréntesis derecho) Entonces
         Mientras (PILA[TOPE] != '(') Repetir
            Llamar a Quita con PILA y TOPE
            Agregar símbolo a EPOS
         Fin Mientras
         Llamar a Quita con PILA y TOPE  // Quita el paréntesis izquierdo
      Si no
         Mientras (PILA no esté vacía y prioridad del símbolo sea <= prioridad del operador en PILA[TOPE]) Repetir
            Llamar a Quita con PILA y TOPE
            Agregar símbolo a EPOS
         Fin Mientras
         Llamar a Pone con PILA y TOPE
      Fin Si
   Fin Mientras
   Mientras (PILA no esté vacía) Repetir
      Llamar a Quita con PILA y TOPE
      Agregar símbolo a EPOS
   Fin Mientras
Fin Algoritmo
```

#### **Explicación**:
- **Entrada**: La expresión infija **EI**.
- **Proceso**:
  1. Recorre la expresión infija.
  2. Usa una pila para manejar operadores y paréntesis.
  3. Mueve los operadores a la expresión postfija según las reglas de precedencia.
- **Salida**: La expresión convertida en **notación postfija**.

---

#### 6. **Conv_prefija (Conversión de infija a prefija)**

Este algoritmo convierte una expresión en **notación infija** a **notación prefija**. La conversión es similar a la postfija, pero la expresión se recorre de derecha a izquierda.

```pseudo
Algoritmo Conv_prefija (EI, EPRE)
   Hacer TOPE ← 0
   Mientras (EI no sea cadena vacía) Repetir
      Tomar el símbolo más a la derecha de EI
      Si (símbolo es un operando) Entonces
         Agregar símbolo a EPRE
      Si no Si (símbolo es un paréntesis derecho) Entonces
         Llamar

 a Pone con PILA y TOPE
      Si no Si (símbolo es un paréntesis izquierdo) Entonces
         Mientras (PILA[TOPE] != ')') Repetir
            Llamar a Quita con PILA y TOPE
            Agregar símbolo a EPRE
         Fin Mientras
         Llamar a Quita con PILA y TOPE
      Si no
         Mientras (PILA no esté vacía y prioridad del símbolo sea <= prioridad del operador en PILA[TOPE]) Repetir
            Llamar a Quita con PILA y TOPE
            Agregar símbolo a EPRE
         Fin Mientras
         Llamar a Pone con PILA y TOPE
      Fin Si
   Fin Mientras
   Invertir EPRE  // Se invierte al final para obtener la notación prefija
Fin Algoritmo
```

#### **Explicación**:
- **Entrada**: La expresión infija **EI**.
- **Proceso**:
  1. Recorre la expresión de derecha a izquierda.
  2. Utiliza una pila para manejar operadores y paréntesis.
  3. Convierte la expresión en **notación prefija**.
- **Salida**: La expresión convertida en **notación prefija**.

---

#### 7. **Evaluación_postfija**

El algoritmo **Evaluación_postfija** evalúa una expresión aritmética en notación **postfija** utilizando una pila para manejar los operandos.

```pseudo
Algoritmo Evaluación_postfija (EPOS, PILA)
   Hacer TOPE ← 0
   Mientras (EPOS no sea cadena vacía) Repetir
      Tomar el símbolo más a la izquierda de EPOS
      Si (símbolo es un operando) Entonces
         Llamar a Pone con símbolo
      Si no (es un operador) Entonces
         Llamar a Quita dos veces para obtener operandos
         Aplicar operación
         Llamar a Pone con resultado
   Fin Mientras
   Llamar a Quita para obtener resultado final
Fin Algoritmo
```

#### **Explicación**:
- **Entrada**: La expresión en notación postfija **EPOS**.
- **Proceso**:
  1. Recorre la expresión postfija.
  2. Al encontrar un operador, se aplican las operaciones sobre los operandos almacenados en la pila.
  3. Se almacena el resultado en la pila.
- **Salida**: El resultado final de la evaluación de la expresión postfija.

---

## **3.3 Colas (FIFO - First In, First Out)**

### **Definición de Colas**

Una cola es una estructura de datos que sigue el principio de **Primero en Entrar, Primero en Salir (FIFO)**. Los elementos se insertan en el **final** de la cola y se eliminan del **frente**.

#### **Ejemplos Prácticos de Colas**:
- **Colas de impresión**: Los documentos que se envían a imprimir se colocan en una cola y se imprimen en el orden en que fueron enviados.
- **Gestión de procesos en sistemas operativos**: Los procesos listos para ejecutarse se colocan en una cola y se ejecutan en el orden en que fueron agregados.

### **Operaciones en Colas**:
Las operaciones básicas que se pueden realizar sobre una cola incluyen:
1. **Cola_vacía**: Verifica si la cola está vacía.
2. **Cola_llena**: Verifica si la cola está llena.
3. **Inserta_cola (Enqueue)**: Inserta un nuevo elemento al final de la cola.
4. **Elimina_cola (Dequeue)**: Elimina el elemento en el frente de la cola.

### **Algoritmos para Colas**

#### 8. **Cola_vacía**

Este algoritmo verifica si la cola está vacía comparando si **FRENTE** es igual a 0.

```pseudo
Algoritmo Cola_vacía (COLA, FRENTE, BAND)
   Si (FRENTE == 0) Entonces
      BAND ← VERDADERO  // La cola está vacía
   Sino
      BAND ← FALSO      // La cola no está vacía
   Fin Si
Fin Algoritmo
```

#### **Explicación**:
- **Entrada**: El valor de **FRENTE**.
- **Salida**: El valor de **BAND** será verdadero si la cola está vacía, de lo contrario, será falso.

---

#### 9. **Cola_llena**

El algoritmo **Cola_llena** revisa si la cola ha alcanzado su tamaño máximo, comparando el valor de **FINAL** con el tamaño máximo **MAX**.

```pseudo
Algoritmo Cola_llena (COLA, FINAL, MAX, BAND)
   Si (FINAL == MAX) Entonces
      BAND ← VERDADERO  // La cola está llena
   Sino
      BAND ← FALSO      // La cola no está llena
   Fin Si
Fin Algoritmo
```

#### **Explicación**:
- **Entrada**: El valor de **FINAL** y el tamaño máximo **MAX** de la cola.
- **Salida**: El valor de **BAND** será verdadero si la cola está llena, de lo contrario, será falso.

---

#### 10. **Inserta_cola (Enqueue)**

El algoritmo **Inserta_cola** agrega un nuevo elemento al final de la cola. Si la cola está llena, muestra un mensaje de **desbordamiento**.

```pseudo
Algoritmo Inserta_cola (COLA, MAX, FRENTE, FINAL, DATO)
   Si (FINAL < MAX) Entonces
      FINAL ← FINAL + 1
      COLA[FINAL] ← DATO
      Si (FRENTE == 0) Entonces
         FRENTE ← 1
      Fin Si
   Sino
      Escribir "Desbordamiento - Cola llena"
   Fin Si
Fin Algoritmo
```

#### **Explicación**:
- **Entrada**: El valor de **FRENTE**, **FINAL**, el tamaño máximo **MAX** y el **DATO** que se desea insertar.
- **Proceso**:
  1. Verifica si la cola está llena.
  2. Si no está llena, incrementa **FINAL** y almacena el nuevo dato en esa posición.
  3. Si **FRENTE** es 0, inicializa su valor.
- **Salida**: La cola con el nuevo elemento insertado.

---

#### 11. **Elimina_cola (Dequeue)**

El algoritmo **Elimina_cola** elimina el elemento que se encuentra en el frente de la cola.

```pseudo
Algoritmo Elimina_cola (COLA, FRENTE, FINAL, DATO)
   Si (FRENTE != 0) Entonces
      DATO ← COLA[FRENTE]
      Si (FRENTE == FINAL) Entonces
         FRENTE ← 0
         FINAL ← 0
      Sino
         FRENTE ← FRENTE + 1
      Fin Si
   Sino
      Escribir "Subdesbordamiento - Cola vacía"
   Fin Si
Fin Algoritmo
```

#### **Explicación**:
- **Entrada**: El valor de **FRENTE** y **FINAL**.
- **Proceso**:
  1. Verifica si la cola está vacía.
  2. Si no está vacía, elimina el dato en **FRENTE** y actualiza los índices.
  3. Si la cola tenía un solo elemento, reinicia los valores de **FRENTE** y **FINAL**.
- **Salida**: El dato eliminado de la cola.

---

#### 12. **Cola_circular**

Este algoritmo implementa una **cola circular**, donde el índice **FINAL** puede "volver" al inicio del arreglo cuando hay espacio disponible.

```pseudo
Algoritmo Inserta_cola_circular (COLA, MAX, FRENTE, FINAL, DATO)
   Si ((FINAL + 1) % MAX == FRENTE) Entonces
      Escribir "Desbordamiento - Cola llena"
   Sino
      FINAL ← (FINAL + 1) % MAX
      COLA[FINAL] ← DATO
      Si (FRENTE == 0) Entonces
         FRENTE ← 1
      Fin Si
   Fin Si
Fin Algoritmo
```

#### **Explicación**:
- **Entrada**: El valor de **FRENTE**, **FINAL**, el tamaño máximo **MAX** y el **DATO** a insertar.
- **Proceso**:
  1. Verifica si la cola está llena (la cola está llena si el siguiente índice de **FINAL** es igual a **FRENTE**).
  2. Si hay espacio, calcula la nueva posición de **FINAL** usando el operador **modulo** para "circular" el índice en el arreglo.
  3. Si **FRENTE** es 0, inicializa su valor.
- **Salida**: La cola actualizada con el nuevo elemento insertado en la posición circular.

---

### **Aplicaciones de Pilas y Colas**

#### **Aplicaciones de Pilas**:
- **Llamadas a Subprogramas**: Las pilas se utilizan para almacenar el estado de las llamadas a funciones o subprogramas.
- **

Recursividad**: La recursividad utiliza pilas para almacenar el estado de las llamadas a funciones en cada nivel de recursión.
- **Tratamiento de Expresiones Aritméticas**: Las pilas son útiles para convertir y evaluar expresiones aritméticas en notación postfija o prefija.

#### **Aplicaciones de Colas**:
- **Gestión de Procesos en Sistemas Operativos**: Los procesos listos para ejecutarse se colocan en una cola y se ejecutan en el orden en que ingresaron.
- **Colas de Impresión**: Los documentos enviados a una impresora se colocan en una cola de impresión y se procesan en el orden en que fueron enviados.
- **Sistemas de Mensajería**: Los mensajes en aplicaciones de mensajería se colocan en una cola y se procesan en orden de llegada.

---

### **Conclusión**

Las pilas y colas son estructuras de datos fundamentales que permiten organizar y procesar los datos de forma eficiente. Las pilas siguen el principio **LIFO** y son útiles en problemas que requieren acceder al último elemento insertado, como la recursividad y las llamadas a funciones. Las colas siguen el principio **FIFO** y son comunes en sistemas donde el orden de llegada determina el orden de atención, como en la gestión de procesos y colas de impresión.

Dominar el uso de estas estructuras es esencial para resolver problemas computacionales de manera eficiente.

---

## En El Siguiente Archivo se Comparten Ejemplos de Aplicación