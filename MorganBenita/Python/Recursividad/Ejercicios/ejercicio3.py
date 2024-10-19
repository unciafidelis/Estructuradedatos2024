import numpy as np

def invertirArreglo(arr,inicio,fin):
    if inicio >= fin:
        return
    arr[inicio],arr[fin] = arr[fin], arr[inicio]
    invertirArreglo(arr,inicio+1,fin-1)
    return arr

A = np.array([1,2,3,4,5])
fin = len(A)-1
print(f"Arreglo original {A}")
print(f"Arreglo invertido {invertirArreglo(A,0,fin)}")

