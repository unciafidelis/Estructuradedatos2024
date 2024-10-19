import numpy as np

def invertirArregloIter(arr):
    inicio = 0
    fin = len(arr)-1
    while inicio < fin:
        arr[inicio],arr[fin] = arr[fin], arr[inicio]
        inicio+=1
        fin-=1
    return arr

A = np.array([1,2,3,4,5])
print(f"Arreglo original {A}")
print(f"Arreglo invertido {invertirArregloIter(A)}")