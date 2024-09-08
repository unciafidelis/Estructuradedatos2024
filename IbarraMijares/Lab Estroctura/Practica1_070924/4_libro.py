class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __eq__(self, otro_libro):
        return self.titulo == otro_libro.titulo

    def __lt__(self, otro_libro):
        return self.titulo < otro_libro.titulo

titulo1 = input("Introduce el título del primer libro: ")
autor1 = input("Introduce el autor del primer libro: ")
libro1 = Libro(titulo1, autor1)

titulo2 = input("\nIntroduce el título del segundo libro: ")
autor2 = input("Introduce el autor del segundo libro: ")
libro2 = Libro(titulo2, autor2)

print(f"\n¿Los títulos son iguales? {libro1 == libro2}")
