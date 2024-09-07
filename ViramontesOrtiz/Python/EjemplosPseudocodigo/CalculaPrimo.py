print("inserta un numero entero, para ver cauntos primos imprimir")
n = int(input())
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