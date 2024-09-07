#Luis Miranda Viramontes
arreglo=[10,20,30,40,50]

for i in range(len(arreglo)):
    print(f"Elemento en indice {i} es {arreglo[i]}")

arreglo[2]=100

print("Arreglo modificado", arreglo)

suma=0

for i in range(len(arreglo)):
    suma += arreglo[i]

print(f"la suma de los elementos es: {suma}")
