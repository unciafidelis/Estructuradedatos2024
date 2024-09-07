def primo(n):
    c = 1
    p = 2
    while c <= n:
        d = 2
        esprimo = True
        while d <= p // 2:
            if p % d == 0:
                esprimo = False
                break
            d += 1
        if esprimo:
            print(p, end=', ')
            c += 1
        p += 1

# Solicita al usuario el número hasta el cual buscar números primos
n = int(input("Introduce un número: "))
primo(n)
