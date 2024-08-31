class Rectangulo:
    def __init__(self,  ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor > 0:
            self._ancho = valor
        else:
            print("Ingrese un valor Ancho positivo")
    @property
    def alto(self):
        return self.ancho
    
    @alto.setter
    def alto(self, valor):
        if valor > 0:
            self._alto = valor
        else:
            print("Ingrese una valor Altura positivo")

    def area(self):
        y = self._ancho*self._alto
        return y

    def perimetro(self):
        return 2* (self._ancho + self._alto)

rect = Rectangulo(6,15)

print("Ancho", rect.ancho)
print("Alto", rect.alto)
print("Area", rect.area())
print("Perimetro", rect.perimetro())