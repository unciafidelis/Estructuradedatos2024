import numpy as np

def euclides(M,N):
    if N == 0:
        return M
    else:
        return euclides(N,M%N)
    
print(euclides(25680,11892))