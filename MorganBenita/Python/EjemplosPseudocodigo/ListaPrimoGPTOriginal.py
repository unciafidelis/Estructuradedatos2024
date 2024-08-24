import time
n = int(input())  # Leer un número entero y asignarlo a n
def func(n):
    start_time = time.time()
    c = 1  # Inicializar c como 1
    p = 2  # Inicializar p como 2
    d = 2  # Inicializar d como 2

    while c <= n:  # Mientras c sea menor o igual a n
        if p % d == 0:  # Si el resto de p dividido por d es igual a 0
            if p == d:  # Si p es igual a d
                print(p)  # Mostrar en pantalla el valor de p
                c += 1  # Incrementar c en 1
            d = 2  # Asignar 2 a d
            p += 1  # Incrementar p en 1
        else:
            d += 1  # Incrementar d en 1
    end_time = time.time() 
    return end_time - start_time

print("Tiempo de ejecución:", func(n), "segundos")
