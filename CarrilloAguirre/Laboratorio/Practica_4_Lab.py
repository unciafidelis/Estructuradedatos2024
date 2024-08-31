class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self):
        cantidad = int(input("Introduce la cantidad deseada de celulares: "))  # Solicita al usuario que ingrese la cantidad deseada
        if cantidad <= self.stock:
            print(f"Producto disponible, su precio es de: ${self.precio}")
            return cantidad  # Devuelve la cantidad solicitada si está disponible
        else:
            print("No hay suficiente stock.")
            return None  # Devuelve None si no hay suficiente stock

    def aplicar_descuento(self, cantidad):
        porcentaje_descuento = float(input("Introduce el porcentaje de descuento (0-100%): "))  # Solicitar al usuario que ingrese el porcentaje de descuento
        if 0 <= porcentaje_descuento <= 100:
            nuevo_precio = self.precio - (self.precio * (porcentaje_descuento / 100)) #Calcular el nuevo precio con descuento
            total = nuevo_precio * cantidad
            print(f"Nuevo precio unitario después del descuento: {nuevo_precio}")
            print(f"Total a pagar por {cantidad} unidades: {nuevo_precio * cantidad}")
        else:
            print("Error: El porcentaje debe estar entre 0% y 100%.")

# Crear un producto con nombre, precio inicial y stock disponible
producto = Producto("Celular", 2000, 10)

# Verificar disponibilidad de la cantidad solicitada
cantidad_solicitada = producto.verificar_disponibilidad()

# Si hay suficiente stock, aplicar descuento y calcular el total
if cantidad_solicitada is not None:
    producto.aplicar_descuento(cantidad_solicitada)





