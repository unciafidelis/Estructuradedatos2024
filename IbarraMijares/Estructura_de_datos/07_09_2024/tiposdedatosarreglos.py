import numpy as np

arreglo = []
arreglo.append(3) # asignar al ultimo espacio
arreglo.append("x")
arreglo.append(3.14)
print(arreglo)# no es arreglo por que varia su tipo no es homogeneo pasa ser unalista de elementos

a = np.array([1])
a = np.append(a,[23,5])
print(a)

#String > Float > Int > Boolean