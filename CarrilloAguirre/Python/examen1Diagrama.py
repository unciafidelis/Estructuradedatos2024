#INICIO
print("INICIO")

#Introduce el valor de n
n = int(input("Introduce el valor n: "))

#Valores de c, p y d
c = 1 #Contador
p = 2 #Número primo
d = 2 #Divisor

while c <= n: #Mientras c sea menor o igual que n se pasara a d y FIN

    if p % d == 0: #Si p se puede dividr con d

        if p == d: #Si p es igual a d

            print(p)  # Imprime p

            c += 1  #c + 1
            p += 1  #p + 1
            d = 2  #d = 2

        else: #Si p es igual a d entonces
            d = 2 #d es igual a 2
            p += 1 #p + 1
    else:
        d += 1 #Sino se pede dividir p con d entonces d + 1

print("FIN")