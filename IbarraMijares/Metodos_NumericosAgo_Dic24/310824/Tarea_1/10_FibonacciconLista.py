n = int(input("Cuantos numeros se desean imorimir en la serie Fibonacci"))
fib = [0, 1]
for i in range(n - 2):
    fib.append(fib[-1] + fib[-2])
    print("-".join(map(str, fib)))


