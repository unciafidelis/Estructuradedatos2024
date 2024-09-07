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

Circulo = Circulo(5)
Rectangulo = Rectangulo(4, 6)



print("Area del Circulo", Circulo.calcular_area())
print("Area del Rectangulo",Rectangulo.calcular_area())



