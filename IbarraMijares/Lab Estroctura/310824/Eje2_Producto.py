class Producto:
    def __init__(self, nombre, precio, disponibilidad):
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad = disponibilidad

    def aplicar_descuento(self, porcentaje):
        if (porcentaje > 0 and porcentaje <= 100):
            