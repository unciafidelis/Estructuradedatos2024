import time
n = int(input())
def func(n):
    start_time = time.time()
    c = 1
    p = 2
    d = 2
    while c <= n:
        if p % d == 0:
            if p == d:
                print(p)
                c += 1
            d = 2
            p += 1
        else:
            d += 1
    end_time = time.time() 
    return end_time - start_time

print("Tiempo de ejecución:", func(n), "segundos")
