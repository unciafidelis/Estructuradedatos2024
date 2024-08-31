class Estudiante:
    def _init_ (self,nombre,calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def evaluar(self):
        if self.calificacion >= 60:
            print(f"{self.nombre} ha aprobado con una calificaccion de {self.calificacion}")
        else:
            print(f"{self.nombre} ha aprobado con una calificacion de : {self.calificacion}")

    def mejorar_calificacion(self, incremento):
        if incremento > 0:
            self.calificacion += incremento
            print(f"Nueva calificacion de {self.nombre}: {self.calificacion}")
        else:
            print("El incremento debe ser positivo")
            
    nombre1= input("Ingrese el nombre del estudiante: ")
    calif = float(input ("Ingrese su calificacion"))
    estudiante1 = Estudiante(nombre, calif)