# Programa examen 1 - diagrama de flujo a python 

def primo(n):
    c=1
    p=2
    d=2

    while c <= n:
        if p%d == 0:
            if p == d:
                print (p)
                c += 1
            d = 2
            p = p + 1
        else:
            d = d + 1
n = int(input("Cuántos números primos quiéres?:  "))
primo(n)