conjunto1 = set(input("Ingresar los elementos para el conjunto 1 separado por una coma").split(","))
conjunto2 = set(input("Ingresar los elemento para el conjunto 2 separados por una coma").split(","))

union = conjunto1 | conjunto2
print("Union de los conjuntos ",union)
insercion = conjunto1 & conjunto2
print("Interseccion de los conjuntos ", insercion)
