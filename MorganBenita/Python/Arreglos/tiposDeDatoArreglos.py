import numpy as np
arreglo = [1,"a",True]
print(arreglo)
arreglo.append(3)
arreglo.append("x")
arreglo.append(3.14)

a = np.array([True])
b = np.array([[1,2,3], [4,5,6], [7,8,9]])
a = np.append(a, [True, False, True])
b[0,0]= 99
b = np.append(b,[[0,0,0],[0,0,0],[0,0,0]], axis=0) # Se agrega axis=0 para insertar nuevos elementos en un array bidimensional
#print(a)
print(b)
print(ord('\\'))

# String > Float > Int > Boolean
                                                                                   
