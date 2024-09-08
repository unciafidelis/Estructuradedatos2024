class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

class Calculadora_Area:
    def calcular_area(self, figura):
        return figura.area()


radio = float(input("Introduce el radio del círculo: "))
circulo = Circulo(radio)

largo = float(input("Introduce el largo del rectángulo: "))
ancho = float(input("Introduce el ancho del rectángulo: "))
rectangulo = Rectangulo(largo, ancho)

calculadora = Calculadora_Area()


print("Área del círculo:", calculadora.calcular_area(circulo))
print("Área del rectángulo:", calculadora.calcular_area(rectangulo))
