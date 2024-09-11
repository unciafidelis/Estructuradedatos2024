nombre = input("Ingresar los nombres separados por una coma").split(",")
edad = input("Ingresar las edades separadas por una coma").split(",")

diccionario = dict(zip(nombre,edad))

print(diccionario)
