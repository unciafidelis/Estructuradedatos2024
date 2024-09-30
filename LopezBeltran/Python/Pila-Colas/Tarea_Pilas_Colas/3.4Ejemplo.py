# Ejemplo 3.4
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

    def invertir(self, exp):
        return exp[::-1]

    def infijo_a_prefijo(self, exp):
        exp = self.invertir(exp)
        exp = exp.replace('(', 'temp').replace(')', '(').replace('temp', ')')
        posfijo = self.infijo_a_posfijo(exp)
        prefijo = self.invertir(posfijo)
        return prefijo

# Ejemplo de uso
converter = Converter()

# Caso a
exp1 = "X + Z * W"
prefijo1 = converter.infijo_a_prefijo(exp1.replace(" ", ""))
print(f"Expresión infija: {exp1}")
print(f"Expresión prefija: {prefijo1}")

# Caso b
exp2 = "(X + Z) * W / T ^ Y - V"
prefijo2 = converter.infijo_a_prefijo(exp2.replace(" ", ""))
print(f"Expresión infija: {exp2}")
print(f"Expresión prefija: {prefijo2}")
