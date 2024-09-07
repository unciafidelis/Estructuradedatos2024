class Ecuacion:
    def __init__(self):
        self.x = self.x = float(input("Introduce numero para dar  valor a X: "))   

    def calcular_y(self):
        return 3 * self.x ** 2 + 7 * self.x - 15

    def imprimir_y(self):
        print(f"El numero ingresado para X es {self.x} el resultado de Y es: {self.calcular_y()}")

    def modificar_x(self, nuevo_x):
        self.x = nuevo_x
        print(f"El numero ingresado para cambiar el valor de  X ha sido modificado a: {self.x}")

ecuacion = Ecuacion()
ecuacion.imprimir_y()  

nuevo_x = float(input("Introduce un nuevo numero para dar valor a X: "))
ecuacion.modificar_x(nuevo_x)
ecuacion.imprimir_y()
