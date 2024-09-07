def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def cuenta_primos(n):
    contador = 0
    for i in range(2, n + 1):
        if es_primo(i):
            contador += 1
    return contador

n = int(input("Ingrese un número entero: "))
print("La cantidad de números primos menores o iguales a", n, "es:", cuenta_primos(n))
