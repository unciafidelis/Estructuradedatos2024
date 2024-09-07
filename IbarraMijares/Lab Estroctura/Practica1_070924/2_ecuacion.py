class Ecuacion:
    def __init__(self,x , y):
        self.x = x
        self.y = y
    def calcuar_ecuacion(self):
        return 3*x**2 + 7*x - 15


    def imprimir_ecuacion(self):
        y = self.calcuar_ecuacion()
        print(f"El valor de Y para  X = {self.x} es : {y}")