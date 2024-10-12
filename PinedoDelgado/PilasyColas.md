# PILAS Y COLAS
> Las *pilas* y *colas*, que son estructuras
de datos lineales con restricciones en cuanto a la posición en la cual se pueden llevar a
cabo las operaciones de inserción y eliminación de componentes.

## Pilas
> Representan una estructura lineal de datos en la que se puede agregar o quitar elementos únicamente por uno de los dos extremos. Se les conoce como *LIFO* (*Last-Input, First-Output*: el último en entrar es el primero en salir).
* Desbordamient pilla llena y s eintenta ingresar un elemto más.
* Push ingresar un elemnto a la pila.
* Pop eliminar un elemto de la pila.

![pilas](pilas.png)

### Operaciones con Pilas
* Push (ingresa dato)
    ![Algoritmo3.3](algoritmo33.png)
    Codigo en Python
    
    '''python 

        def pila_llena(tope, max_size):
        # Verifica si la pila está llena
        return tope == max_size

        def pone(pila, tope, max_size, dato):
            # Verificar si la pila está llena
            band = pila_llena(tope, max_size)

            if band:
                print("Desbordamiento - Pila llena")
            else:
                # Actualiza TOPE e inserta el nuevo elemento en el TOPE de PILA
                tope += 1
                pila[tope] = dato
                return tope  # Retorna el nuevo TOPE

    '''
* Pop (elimina dato)
    ![Algoritmo 3.4](algoritmo34.png)

    Codigo en Python

    '''python

        def pila_vacia(tope):
        # Verifica si la pila está vacía
        return tope == -1

        def quita(pila, tope):
            # Verificar si la pila está vacía
            band = pila_vacia(tope)

            if band:
                print("Subdesbordamiento - Pila vacía")
            else:
                # Elimina el elemento en la posición TOPE
                dato = pila[tope]
                tope -= 1  # Actualiza TOPE
                return dato, tope  # Retorna el DATO eliminado y el nuevo TOPE
    '''

* Pila vacía
    ![Algoritmo 3.4](algoritmo31.png)
    
    Código en Python

    ''' python

        def pila_vacia(tope):
            # BAND se asigna a True si la pila está vacía, False si no
            if tope == 0:
                band = True  # La pila está vacía
            else:
                band = False  # La pila no está vacía
            return band    
    '''

* Pila llena
    ![Altgoritmo 3.2](algoritmo32.png)
    
        Codigo en Python
        
        '''python

            def pila_llena(tope, max_size):
            # BAND se asigna a True si la pila está llena, False si no
            if tope == max_size:
                band = True  # La pila está llena
            else:
                band = False  # La pila no está llena
            return band
        '''
### Ejemplo 3.1
Si se insertaran los elementos lunes, martes, miércoles, jueves y viernes en PILA, la
estructura quedaría tal y como se muestra el codigo del ejemplo 3.1. 
Ahora bien, si se elimina el elemento viernes, el TOPE apuntaría ahora a jueves.
Si en algún momento se quisiera eliminar al elemento martes, esto no sería posi
ya que sólo se puede tener acceso al elemento que se encuentra en la cima de la pila y paar resolver se debe eliminar miercoles hasta dejar como TOPE el martes.

Solución: 

![Ejemplo 3.1](ejemplo31.png)

### Aplicaciones con Pilas

* Llamadas a subprogramas
>* También conocido como módulo o función, internamente se usan pilas para guardar el estado de las variables del programa, así como instrucciones pendientes de ejecución en el momento que se hace la llamada.
> * Cuando termina la ejecución del subprograma, los valores almacenad
en la pila se recuperan para continuar con la ejecución del programa en el punto en
cual fue interrumpido.
>* Además de las variables se recupera la dirección del programa
la que se hizo la llamada, porque a esa posición se regresa el control del proceso.

![Llamadas a subprogramas](subprograma.png)

* ### Recursividad
* ### Tratamiento de expresiones aritméticas
      Un problema interesante en computación consiste en convertir expresiones en notación
      infija a su equivalente en notación prefija o posfija o prefija. S
    * Dada la expresión A + B se dice que ésta se encuentra en notación infija.
      operador (+) se encuentra entre los operandos (A y B).
    
    * Dada la expresión AB+ se dice que ésta se encuentra en notación postfija, po
      el operador (+) se encuentra después de los operandos (A y B).

    * Dada la expresión +AB se dice que ésta se encuentra en notación prefija, porque=
      operador (+) está precediendo a los operandos (A y B).


    * Solamente se manejarán los siguientes operadores -se presentan de mayor a Gl:
      nor según sea su prioridad de ejecución-:

       ![Operadores Aritmeticos](operadores.png)
      
    * Los operadores de más alta prioridad se ejecutan primero.
    * Si hubiera en una expresión dos o más operadores de igual prioridad, entonces
      procesarán de izquierda a derecha.
    * Las subexpresiones que se encuentran entre paréntesis tendrán más prioridad
      cualquier operador.

* Ordenación

Otra aplicación de las pilas se puede ver en el método de ordenación rápida.

### Ejemplo 3.3 
Traducción de notación infija a posfija. 

    '''
        class Pila:
            def __init__(self, max_size):
                self.items = []
                self.max_size = max_size

            def is_empty(self):
                return len(self.items) == 0

            def push(self, item):
                if len(self.items) < self.max_size:
                    self.items.append(item)

            def pop(self):
                if not self.is_empty():
                    return self.items.pop()

            def top(self):
                if not self.is_empty():
                    return self.items[-1]

        def prioridad(operador):
            if operador == '+' or operador == '-':
                return 1
            elif operador == '*' or operador == '/':
                return 2
            elif operador == '^':
                return 3
            return 0

        def conv_postfija(expresion_infixa):
            max_size = len(expresion_infixa)
            pila = Pila(max_size)
            expresion_postfija = ""
            
            for simbolo in expresion_infixa:
                if simbolo.isalnum():  # Si es un operando
                    expresion_postfija += simbolo
                elif simbolo == '(':
                    pila.push(simbolo)
                elif simbolo == ')':
                    while not pila.is_empty() and pila.top() != '(':
                        expresion_postfija += pila.pop()
                    pila.pop()  # Quitar () de la pila
                else:  # Si es un operador
                    while (not pila.is_empty() and
                        prioridad(simbolo) <= prioridad(pila.top())):
                        expresion_postfija += pila.pop()
                    pila.push(simbolo)

            while not pila.is_empty():
                expresion_postfija += pila.pop()

            return expresion_postfija

        # Ejemplo de uso
        expresion_infixa = "X+Z*W"
        resultado = conv_postfija(expresion_infixa)
        print("Expresión postfija:", resultado)
              
    '''
![Resultado Ejemplo 3.2](Resultadoejemplo32.png)

## COLAS
>Una *cola* constituye una estructura lineal de datos en la que los nuevos elementos se
introducen por un extremo y los ya existentes se eliminan por el otro. Debido a esta característica, las colas también reciben el
nombre de estructuras *FIFü* (First-In, First-Out: el primero en entrar es el primero en
salir).

### Representación de colas
>Este tipo de estructura de datos se puede representar mediante diante el uso de:
    • Arreglos    
    • Listas
Cuando se implementan con arreglos unidimensionales, es importante definir
tamaño máximo para la cola y dos variables auxiliares. Una de ellas para que al
cene la posición del primer elemento de la cola -FRENTE- y otra para que guaro:
la posición del último elemento de la cola -FINAL-.

![Presentacion de colas](colas1.png)

### Operaciones con colas
>La definición de la estructura de datos tipo cola queda completa al incluir las operaciones que se pueden realizar en ella. Las operaciones básicas que pueden efectuarse son:

• Insertar un elemento en la cola

• Eliminar un elemento de la cola

Las inserciones se llevarán a cabo por el FINAL de la cola, mientras que las eliminaciones se harán por el FRENTE -recuerde que el primero en entrar es el primero en salir-.

* Insertar cola
    Algoritmo 3.7
![Insertar cola](insertacola.png)
Codigo Pythpon
'''python
class Cola:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cola = [None] * max_size
        self.final = -1  # Indica el último índice ocupado
        self.frenete = -1  # Indica el índice del primer elemento

    def insertar(self, dato):
        if self.final < self.max_size - 1:  # Verifica que hay espacio libre
            self.final += 1  # Actualiza FINAL
            self.cola[self.final] = dato  # Agrega el dato a la cola

            if self.final == 0:  # Se insertó el primer elemento
                self.frenete = 0  # Actualiza FRENTE
        else:
            print("Desbordamiento - Cola llena")  # Mensaje de error

    def mostrar(self):
        if self.final >= 0:
            print("Contenido de la cola:", self.cola[:self.final + 1])
        else:
            print("La cola está vacía.")

        # Ejemplo de uso
        tamaño_maximo = 5
        cola = Cola(tamaño_maximo)

        # Insertar elementos
        cola.insertar(10)
        cola.insertar(20)
        cola.insertar(30)
        cola.insertar(40)
        cola.insertar(50)
        cola.insertar(60)  # Este debería mostrar un mensaje de desbordamiento

        # Mostrar contenido de la cola
        cola.mostrar()

'''
![Desbordamiento de Cola](colallena.png)

* Elimina Cola
    Algoritmo 3.8
![Eliminar Cola](eliminarcola.png)
Codigo en Python

'''python

        class Cola:
            def __init__(self, max_size):
                self.max_size = max_size
                self.cola = [None] * max_size
                self.frenete = -1  # Indica el índice del primer elemento
                self.final = -1  # Indica el último índice ocupado

            def insertar(self, dato):
                if self.final < self.max_size - 1:  # Verifica que hay espacio libre
                    self.final += 1  # Actualiza FINAL
                    self.cola[self.final] = dato  # Agrega el dato a la cola

                    if self.final == 0:  # Se insertó el primer elemento
                        self.frenete = 0  # Actualiza FRENTE
                else:
                    print("Desbordamiento - Cola llena")  # Mensaje de error

            def eliminar(self):
                if self.frenete >= 0:  # Verifica que la cola no esté vacía
                    dato = self.cola[self.frenete]  # Almacena el primer elemento
                    if self.frenete == self.final:  # Si hay un solo elemento
                        self.frenete = -1  # Indica COLA vacía
                        self.final = -1
                    else:
                        self.frenete += 1  # Mueve FRENTE al siguiente elemento
                    return dato        

'''

* Cola Vacía
    Algoritmo 3.9
    Cola_vacía (COLA, FRENTE, BAND)
    Este algoritmo determina si una estructura de datos tipo cola está vacía, asignando a
    el valor de verdad correspondiente
    1. Si (FRENTE =O)
    entonces
    Hacer BAND +- VERDADERO
    si no
    Hacer BAND +- FALSO
    2 {Fin del condicional del paso l}
    Algoritmo 3 10 Cola_llen

codigo en Python
'''python

        def cola_vacia(frente):
            # Inicializamos BAND como FALSO
            band = False
            
            # Verificamos si el FRENTE es igual a 0
            if frente == 0:
                band = True  # La cola está vacía
            else:
                band = False  # La cola no está vacía
            
            return band

        # Ejemplo de uso
        frente = 0  # Por ejemplo, el número de elementos en la cola

        # Llamamos a la función y mostramos el resultado
        if cola_vacia(frente):
            print("La cola está vacía.")
        else:
            print("La cola no está vacía.")

'''

* Cola Llena
    ![Cola llena](colallena2.png)

    '''python

            def cola_llena(final, max):
            # Inicializamos BAND como FALSO
            band = False
            
            # Verificamos si FINAL es igual a MAX
            if final == max:
                band = True  # La cola está llena
            else:
                band = False  # La cola no está llena
            
            return band

        # Ejemplo de uso
        final = 5  # Por ejemplo, el número actual de elementos en la cola
        max = 5    # Capacidad máxima de la cola

        # Llamamos a la función y mostramos el resultado
        if cola_llena(final, max):
            print("La cola está llena.")
        else:
            print("La cola no está llena.")
    '''

## Ejemplo 3.6
'''
        class Cola:
            def __init__(self, max_size):
                self.max_size = max_size
                self.cola = []

            def encolar(self, dia):
                if self.size() < self.max_size:
                    self.cola.append(dia)
                    print(f"{dia} agregado a la cola.")
                else:
                    print("Desbordamiento: La cola está llena. No se puede agregar más elementos.")

            def desencolar(self):
                if self.size() > 0:
                    eliminado = self.cola.pop(0)  # Eliminar el primer elemento
                    print(f"{eliminado} eliminado de la cola.")
                else:
                    print("La cola está vacía. No se puede eliminar ningún elemento.")

            def size(self):
                return len(self.cola)

            def mostrar(self):
                if self.size() == 0:
                    print("La cola está vacía.")
                else:
                    print("Contenido de la cola:", self.cola)

        # Ejemplo de uso
        cola = Cola(max_size=7)

        # Agregar días iniciales a la cola
        dias = ["lunes", "martes", "martes", "miércoles", "jueves"]
        for dia in dias:
            cola.encolar(dia)

        # Menú principal
        while True:
            print("\nMenú:")
            print("1. Mostrar cola")
            print("2. Eliminar un elemento del frente")
            print("3. Agregar un nuevo elemento al final")
            print("4. Salir")

            opcion = input("Seleccione una opción (1-4): ")

            if opcion == '1':
                cola.mostrar()
            elif opcion == '2':
                if cola.size() > 0:
                    eliminar = input("Ingrese el día que desea eliminar del frente: ")
                    if eliminar == cola.cola[0]:  # Verificamos si coincide con el frente
                        cola.desencolar()
                    else:
                        print(f"No se puede eliminar {eliminar} porque no es el día en el frente.")
                else:
                    print("No hay elementos en la cola para eliminar.")
            elif opcion == '3':
                nuevo_dia = input("Ingrese el nuevo día que desea agregar al final: ")
                cola.encolar(nuevo_dia)  # Agregar el nuevo día
            elif opcion == '4':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")

'''

## Colas Circulares
>Es una mejora sobre las colas, las colas circulares permiten que se 
reutilicen los espacios que quedan vacíos después de eliminar un 
elemento, utiliza también dos apuntadores: uno para el Frente y otro 
para el Final de la cola.

![Colas Circulares](colascirculares.png)

    * Insertar Cola Circular
![Insertar cola Circular](insercolacircular.png)
