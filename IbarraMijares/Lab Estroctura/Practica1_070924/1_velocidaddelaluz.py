from abc import ABC, abstractmethod
class CalculodedistanciadelaLuz(ABC):
    def __init__(self):
        self.tiempo_segundos = 0
    
    def Ingreso_tiempo(self):
        self.tiempo_segundos = float(input("Introduce el tiempo en segundos: "))

    @abstractmethod
    def imprimir_distancia(self):
        pass

class Distanciarecorrida(CalculodedistanciadelaLuz):
    velocidadluz = 300000

    def imprimir_distancia(self):
        distancia = self.velocidadluz * self.tiempo_segundos
        print(f"La distancia recorrida {self.tiempo_segundos} segundos es: {distancia} km/s")


distancia_luz = Distanciarecorrida()
distancia_luz.Ingreso_tiempo() 
distancia_luz.imprimir_distancia()
