import numpy as np
NTC = (-1 - (-4) + 1) *(2 - (-2) + 1)
caracter = ''
#LETRAS = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
LETRAS = np.zeros((4,5,5),int)
#print(LETRASx)
for i in range(LETRAS.shape[0]):
    for j in range(LETRAS.shape[1]):
        for k in range(LETRAS.shape[2]):
            NTC = (-1 - (i-4) + 1) *(2 - (j-2) + 1)
            #print(ord(chr(NTC)))
            caracter = ord(chr(NTC))
            LETRAS[i,j,k] = caracter
    #LETRAS = np.append(LETRAS,[[0,0,0,0,0]], axis=0)
print(LETRAS)
