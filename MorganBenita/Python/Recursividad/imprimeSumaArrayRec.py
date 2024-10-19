import numpy as np

def array_sum(arr,N):
    if N == 0:
        return N
    else:
        return arr[N-1]+array_sum(arr,N-1) 
A = np.array([1,2,3,4,6])
print(array_sum(A,len(A)))