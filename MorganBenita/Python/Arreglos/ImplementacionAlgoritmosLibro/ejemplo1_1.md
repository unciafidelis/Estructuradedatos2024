# Ejemplo 1.1
Consideremos que en una universidad se conocen 
las calificaciones de un grupo de 50
alumnos. Se necesita saber cuántos de 
éstos tienen calificación superior al promedio del
grupo.

## Algoritmo
1. Hacer AC <- O e I <- 1
2. Mientras (I <= 50) Repetir
Escribir "Ingrese la calificación", I
Leer C
Hacer AC <- AC + C e I <- I + 1
3. (Fin del ciclo del paso 2)
4. Hacer PROM = AC/50
(Como se necesita indicar cuántos alumnos obtuvieron calificación superior al promedio, se
releerán las 50 calificaciones para comparar cada una de ellas con el promedio calculado en
el paso 4)
Hacer CONT <- O e I <- 1
5. Mientras (I <= 50) Repetir
Escribir "Ingrese la calificación", 1
Leer C
    1. Si C > PROM entonces
    Hacer CONT <- CONT + 1
    2. {Fin del condicional del paso 5.1 }
    Hacer I <- I + 1
6. {Fin del ciclo del paso 5}
7. Escribir CONT

```python
# Inicializar el acumulador y el contador
AC = 0
I = 1

# Bucle para pedir 50 calificaciones
while I <= 50:
    # Pedir al usuario que ingrese una calificación
    C = float(input(f"Ingrese la calificación {I}: "))
    
    # Sumar la calificación al acumulador
    AC += C
    
    # Incrementar el contador
    I += 1

# Calcular el promedio
PROM = AC / 50

# Mostrar el resultado
print(f"El promedio de las 50 calificaciones es: {PROM}")

# Inicializar el contador de calificaciones mayores al promedio
CONT = 0
I = 1

# Definir un valor para el promedio
PROM = float(input("Ingrese el valor del promedio: "))

# Bucle para pedir 50 calificaciones
while I <= 50:
    # Pedir al usuario que ingrese una calificación
    C = float(input(f"Ingrese la calificación {I}: "))
    
    # Si la calificación es mayor que el promedio, incrementar el contador
    if C > PROM:
        CONT += 1
    
    # Incrementar el contador de iteraciones
    I += 1

# Mostrar el resultado
print(f"Cantidad de calificaciones mayores que el promedio: {CONT}")
```
