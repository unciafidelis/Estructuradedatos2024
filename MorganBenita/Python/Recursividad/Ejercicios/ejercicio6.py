import numpy as np
def mezclaPaises(SUR,CENTRO,NORTE):
    if len(SUR) == 0:
        return np.concatenate((CENTRO,NORTE))
    elif len(CENTRO) == 0:
        return np.concatenate((SUR,NORTE))
    elif len(NORTE) == 0:
        return np.concatenate((SUR,CENTRO))
    
    if SUR[0] < CENTRO[0] and SUR[0] < NORTE[0]:
        return np.concatenate(([SUR[0]],mezclaPaises(SUR[1:],CENTRO,NORTE)))
    elif CENTRO[0] < SUR[0] and CENTRO[0] < NORTE[0]:
        return np.concatenate(([CENTRO[0]],mezclaPaises(SUR,CENTRO[1:],NORTE)))
    elif NORTE[0] < SUR[0] and NORTE[0] < CENTRO[0]:
        return np.concatenate(([NORTE[0]],mezclaPaises(SUR,CENTRO,NORTE[1:])))

sur = np.array(['Argentina','Bolivia','Colombia'])
centro = np.array(['Belize','Costa Rica', 'El Salvador', 'Guatemala'])
norte = np.array(['Canada', 'Estados Unidos', 'México'])

print(mezclaPaises(sur,centro,norte))  

#Imprime con error el resultado

