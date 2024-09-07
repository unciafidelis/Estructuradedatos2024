
from abc import ABC, abstractmethod

class calculardistancia(ABC):
    velocidadluz = 300000
    def tiempoensegundos(self):
        pass

    def imprimir_distancia_segundos(self):
        pass

class calculardistanciaensegundos(calculardistancia):
    def __init__(self,tiempoensegundos):
        self.tiempoensegundos = tiempoensegundos
    
    def ingreso_tiempoensegundos(self):
        return self.tiempoensegundos

    def imprimir_distancia_segundos(self):
        distancia = self.velocidadluz * self.tiempoensegundos()
        print(f"La distancia que recorre en {self.ingreso_tiempoensegundos()} segundos en : {distancia} kilometros")

tiempo = float(input("Ingresar tiempo en segundos"))
calculo = calculardistanciaensegundos(tiempo)
calculo.imprimir_distancia_segundos() 
