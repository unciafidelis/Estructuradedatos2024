import time

# Código optimizado
print("Inserta un número entero")
n = int(input())
def func(n):
    start_time = time.time()
    c = 0
    p = 2

    while c < n:
        is_prime = True
        for d in range(2, int(p ** 0.5) + 1):
            if p % d == 0:
                is_prime = False
                break
    
        if is_prime:
            print(p)
            c += 1

        p += 1
    end_time = time.time() 
    return end_time - start_time

print("Tiempo de ejecución:", func(n), "segundos")