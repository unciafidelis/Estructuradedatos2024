class Estudiante:
    def __init__(self, nombre, calificación):
        self.nombre = nombre
        self.calificación = calificación

    def evaluar(self):
        if self.calificación >= 60:
            print(f"{self.nombre} ha aprobado con una calificación de: {self.calificación}")
        else:
            print(f"{self.nombre} ha re  probado con una calificación de: {self.calificación}")


nombre1 = input("Ingrese el nombre del estudiante: ")
calif = float(input("Ingrese su calificación: "))

estudiante1 = Estudiante(nombre1, calif)