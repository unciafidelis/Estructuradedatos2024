import numpy as np
NTC = (-1 -(-4) + 1) * (2 - (-2)+ 1 )
caracter = " "
LETRAS = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
for i in range(LETRAS.shape[0]):
    for j in range(LETRAS.shape[1]):
        NTC = (-1 -(-4) + 1) * (2 - (-2)+ 1 )
        print(ord(chr(NTC)))
        caracter = ord(chr((NTC)))
        LETRAS[i,j] = caracter
print(LETRAS)
