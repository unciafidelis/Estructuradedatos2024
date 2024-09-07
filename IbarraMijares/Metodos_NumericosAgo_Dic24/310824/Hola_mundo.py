print("Hola Mundo")

nombre = input("Dime tu nombre:")
print("Hola "+nombre)

ano_nacimiento = input("Dime tu año de nacimiento separado por  - cada digito")
digito = ano_nacimiento.split("-")
 
numeroSuerte = 0
for digito in digito:
    print(digito, type(digito))
    numeroSuerte += int(digito)
print("Tu numero de la suerte es: " , suma)

if numeroSuerte % 2 == 0:
    print("Tu numero de la suerte es par")
else:
    print("Tu numero de la suerte es impar")