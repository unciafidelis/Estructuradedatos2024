
tupla1 = tuple(map(int, input("Ingresar los elemento de la tupla 1 ").split()))
tupla2 = tuple(map(int, input("Ingresar los elemento de la tupla 2 ").split()))


print("Concatenacon de las Tuplas", tupla1 + tupla2)
print("Suma total de Tupla 1 y Tupla ", sum(tupla1) + sum(tupla2))
print("Revesion de la Tupla 1", tuple(reversed(tupla1)))
print("Reversion de la Tupla 2 ", tuple(reversed(tupla2)))