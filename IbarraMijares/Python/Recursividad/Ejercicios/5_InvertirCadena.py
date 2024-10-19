def invertirCadena(cadena):
    if len(cadena)<= 1:
        return cadena
    else: 
        return invertirCadena(cadena[1:])+cadena[0]

print(invertirCadena("ROMA"))