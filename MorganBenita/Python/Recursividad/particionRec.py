def particion(M,N):
    if M == 0 or N == 0:
        return 0
    elif N>1:
        return 1 + particion(M,N-1)
    else:
        return particion(M-1,N)
    
print(particion(6,6))

### NO ESTA LISTO
