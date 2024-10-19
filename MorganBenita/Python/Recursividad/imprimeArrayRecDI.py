import numpy as np

def imprimir_array_DI(arr,N):
    if N != 0:
        print(arr[N-1])
        imprimir_array_DI(arr,N-1)
    else:
        return
A = np.array([1,2,3,4,6])
print(imprimir_array_DI(A,len(A)))