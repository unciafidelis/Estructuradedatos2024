# Ejemplo 3.2
class Converter:
    def __init__(self):
        self.precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def es_operador(self, c):
        return c in self.precedencia

    def prioridad(self, operador):
        return self.precedencia.get(operador, 0)

    def infijo_a_posfijo(self, exp):
        stack = []
        resultado = []
        for char in exp:
            if char.isalnum():  # Si el caracter es un operando
                resultado.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    resultado.append(stack.pop())
                stack.pop()  # Elimina '('
            else:  # El caracter es un operador
                while (stack and self.prioridad(stack[-1]) >= self.prioridad(char)):
                    resultado.append(stack.pop())
                stack.append(char)

        while stack:
            resultado.append(stack.pop())
        
        return ''.join(resultado)

# Ejemplo de uso
converter = Converter()

# Caso a
exp1 = "X + Z * W"
posfijo1 = converter.infijo_a_posfijo(exp1.replace(" ", ""))
print(f"Expresión infija: {exp1}")
print(f"Expresión posfija: {posfijo1}")

# Caso b
exp2 = "(X + Z) * W / T ^ Y - V"
posfijo2 = converter.infijo_a_posfijo(exp2.replace(" ", ""))
print(f"Expresión infija: {exp2}")
print(f"Expresión posfija: {posfijo2}")
