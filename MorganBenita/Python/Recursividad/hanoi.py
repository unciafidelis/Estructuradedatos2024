def hanoi(N,ORIGEN,DESTINO,AUXILIAR):
    if N==1:
        return print(f"Mover un Disco de {ORIGEN} a {DESTINO}")
    else:
        hanoi(N-1, ORIGEN,AUXILIAR,DESTINO)
        print(f"Mover un Disco de {ORIGEN} a {DESTINO}")
        hanoi(N-1,AUXILIAR,DESTINO,ORIGEN)
print(hanoi(4,"A","B","C"))