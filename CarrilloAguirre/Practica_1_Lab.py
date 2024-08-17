class persona:
    nombre = "Gerardo Carrillo"
    edad = 33
    grado = "Licenciatura"
    peso = "98"
    direccion = "Melchor Ocampo #708-2"
    Estatura = 1.72
    oficio = "Instructor Técnico"
    ciudad = "Calera de Victor Rosales, Zac."
    pais = "Mexico"

    def saludar(self, param_1,param_2, param_3, param_4):
        print(f"Hola me llamo {self.nombre} tengo {self.edad} años de edad y soy de {self.ciudad}, {self.pais}")

    def dar_ubicacion(self):
        print("prueba")

estudiante = persona()

estudiante.saludar("param_1","param_2", "param_3", "param_4")