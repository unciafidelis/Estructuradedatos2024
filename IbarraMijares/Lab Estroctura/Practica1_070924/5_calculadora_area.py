import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area_circulo(self):
        return (math.pi * (radio**2))

class Rectangulo:
    def __init__(self, ancho, largo):
        self.ancho = ancho
        self.largo = largo

    def area_rectangulo(self):
        return largo * ancho

class Calculadora_area:
    def __init__(self):
        pass

    def calcular_area(self, figura):
        return calcular_area()

Circulo = Circulo(5)
Rectangulo = Rectangulo(4, 6)
Calculadora = Calculadora_area()


print("Area del Circulo", Calculadora.calcular_area(Circulo))
print("Area del Rectangulo",Calculadora.calcular_area(Rectangulo))



