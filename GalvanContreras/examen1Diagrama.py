n = int(input("Ingresa el valor de n: "))
c = 1  # Contador de números primos
p = 2  # Primer número primo
d = 2  # Divisor

while c <= n:
    if p % d == 0:
        if p == d:
            # Es primo
            print(f"Primo {c}: {p}")
            c += 1
        d = 2
        p += 1
    else:
        d += 1
