import abc
from abc import ABC
class Operaciones(ABC):
    
    def suma(self):
        pass

    def resta(self):
        pass

    def multlipicacion(self):
        pass

    def division(self):
        pass

class Suma(Operaciones):
    def _init_(self, a, b):
        self.a = a
        self.b = b

    def suma (self):
        return a + b 

class Resta(Operaciones):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def resta(self):
        return a - b


class Multlipicacion(Operaciones):
    def _init_(self, a, b):
        self.a = a
        self.b = b

    def multlipicacion(self):
        return a * b


class Division(Operaciones):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def division(self):
        if b != 0:
            return a/b
        else:
            print("Error: tiene que ser diferente de  cero")

suma = Suma()
resta = Resta()
multlipicacion = Multlipicacion()
division = Division()

print("Suma", suma.suma(5,2))
print("Resta", Resta.resta(5,2))
print("Multlipicacion", multlipicacion.multlipicacion(5,2))
print("Division", division.division(5,2))

