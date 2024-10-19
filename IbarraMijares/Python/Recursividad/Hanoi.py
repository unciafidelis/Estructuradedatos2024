def Hanoi(N,ORIGEN,DESTINO,AUXILAR):
    if N == 1:
        return print("Mover un disco de {ORIGEN} a {DESTINO}")
    else:
        Hanoi(N-1,ORIGEN,DESTINO,AUXILAR)
        print(f"Mover un disco de {ORIGEN} a {DESTINO}")
        Hanoi(N-1,AUXILAR,DESTINO,ORIGEN)
print(Hanoi(4,"A","B","C"))