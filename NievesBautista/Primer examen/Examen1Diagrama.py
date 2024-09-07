"""
Edgar Israel Nieves Bautista
examen 1 resolver el algoritmo

"""

# Solicitar el número al usuario
n = int(input("Ingrese un número: "))

# Inicializar variables
c = 1
p = 2
d = 2

# Mientras c sea menor o igual a n
while c <= n:
    # Si el número p es divisible por d
    if p % d == 0:
        # Si d es igual a p, se imprime p y se incrementa c
        if d == p:
            print(p)
            c += 1
        # Resetear valores de d y p
        d = 2
        p += 1
    else:
        # Incrementar d para probar con el siguiente divisor
        d += 1
#siempre imprimi p, segui tal cual el ejercicio, no se si se nesecitaba hacer una funcion o una clase para resolver