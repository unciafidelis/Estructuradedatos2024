import numpy as np

def determinante(matriz):
    if matriz.shape[0] == 2:
        return matriz[0,0]*matriz[1,1] - matriz[0,1]*matriz[1,0]
    else:
        det = 0
        for i in range(matriz.shape[1]):
            submatriz = np.delete(np.delete(matriz,0,axis=0),i,axis=1)
            cofactor = (-1)**i*matriz[0,i]
            det +=cofactor*determinante(submatriz)
        return det

matriz = np.array([[3,15,1],[6,8,12],[2,9,10]])
print(matriz)
print(determinante(matriz))