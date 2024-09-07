print ("Bienvenido a mi programa")
n = int(input("Introduce un numero : "))
c = 1
p = 2
d = 2

while c <= n:
    if p % d == 0:
        if p == d:
            print(f"{p}")
            c += 1
        d = 2
        p += 1
    else:
        d += 1