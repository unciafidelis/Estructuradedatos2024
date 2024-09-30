#Algoritmo 3.10 Cola llena
#Este algoritmo determina si una estructura de datos tipo cola está llena,
#asignando a BAND el valor de verdad correspondiente
def cola_llena(final,maximo):
    if final == maximo:
        return True
    else:
        return False

#Ejemplo de uso 
final = 3
maximo = 3
band= cola_llena(final,maximo)
print("La cola esta llena:",band)    