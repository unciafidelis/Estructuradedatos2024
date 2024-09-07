class OperacionesBasicas:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        return self.numero1 + self.numero2
    def restar(self):
        return self.numero1 - self.numero2
    def multiplicar(self):
        return self.numero1 * self.numero2
    def dividir(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "Error: División por cero no permitida"

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

operacion = OperacionesBasicas(numero1, numero2)
print("Suma:", operacion.sumar())     
print("Resta:", operacion.restar())      
print("Multiplicación:", operacion.multiplicar())
print("División:", operacion.dividir())
