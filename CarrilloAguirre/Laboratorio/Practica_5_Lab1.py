from abc import ABC, abstractmethod

#Clases abstractas
class OperacionMatematica(ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def suma(self):
        pass
    @abstractmethod
    def resta(self):
        pass
    @abstractmethod
    def multiplicacion(self):
        pass
    @abstractmethod
    def division(self):
        pass

#Clases hijas
class Operaciones(OperacionMatematica):
    def suma(self):
        return self.a + self.b
    def resta(self):
        return self.a - self.b
    def multiplicacion(self):
        return self.a * self.b
    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: División por cero no permitida."

#Ingresar los valores a y b
a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))

#Objeto de la clase Operaciones con los valores a y b
operacion = Operaciones(a, b)

#Llamadas a métodos para realizar cada operación matemática y mostrar resultados
print(f"Suma: {a} + {b} = {operacion.suma()}")
print(f"Resta: {a} - {b} = {operacion.resta()}")
print(f"Multiplicación: {a} * {b} = {operacion.multiplicacion()}")
print(f"División: {a} / {b} = {operacion.division()}")