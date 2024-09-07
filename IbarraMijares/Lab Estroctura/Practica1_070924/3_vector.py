class Vector:
    def __init__(self):
        self.x = float(input("Introduce el valor de X: "))  
        self.y = float(input("Introduce el valor de Y: ")) 

    
    def __mul__(self, escalar):
        return VectorResultado(self.x * escalar, self.y * escalar)

    
    def __rmul__(self, escalar):
        return self.__mul__(escalar)

    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"


class VectorResultado:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v = Vector() 
print("El Vector ingresado por el usuario es:", v)


escalar = float(input("Introduce el escalar para multiplicar el vector: "))

v_escalar = v * escalar
print("Resultado de la mutlipicacion:", v_escalar)
