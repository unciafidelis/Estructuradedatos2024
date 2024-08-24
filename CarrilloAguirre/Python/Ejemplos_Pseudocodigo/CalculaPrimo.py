print("Inserta un número entero")
n = int(input())
c = 1
p = 2
d = 2
while c <= n:
    if p % d == 0:
        if p == d:
            print(f"{p}")
            c += 1 #Incrementales forma 1 forma mas simple y eficiente en memoria
        d = 2
        p = p + 1 #Incrementales forma 2
    else:
        d = d + 1