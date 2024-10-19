pos = int(input('Escriba que posición quiere de la serie de Fibonacci: '))
iniFibo = 0
finFibo = 1
for x in range(0,pos):
    if x == 0:
        finFibo = 0
    elif x == 1:
        finFibo = 1
    sum = finFibo
    finFibo = finFibo + iniFibo
    iniFibo = finFibo - iniFibo
print(f'\nPosición Final: {x+1:>4} -- Valor en la serie de Fibonacci:  {sum:>10}  ')