import numpy as np

def imprimir_array(arr, i=0):
    if i >= len(arr):
        return
    else:
        print(arr[i])
        imprimir_array(arr,i+1)

A = np.array([1,2,3,4,6])
print(imprimir_array(A))