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

