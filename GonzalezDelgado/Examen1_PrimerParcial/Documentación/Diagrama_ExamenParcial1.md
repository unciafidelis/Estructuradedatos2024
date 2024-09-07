# **Diagrama_ExamenParcial1**

---

```py

# Angel Janvier Gonzalez Delgado

# Primer Examen Parcial de Estructura de Datos

# 07/09/2024 v1.0.0

  

# Se Inician las Variables

n = int(input("N es Igual a: (～￣▽￣)～   →"))

c = 1

p = 2

d = 2

  

# Programa Principal, Uso de las Variables

while c <= n:

    if p % d == 0:

        if p == d:

            print(p)

            c = c + 1

        d = 2

        p = p + 1

    else:

        d = d + 1

  
  

# El programa encuentra los primeros n números primos verificando

# la divisibilidad de cada número p y lo imprime si es primo.
```

## **Resultados:**

![[Captura de pantalla 2024-09-07.png]]

## **Explicación:**

- El programa pide un número `n` al usuario.
- Comienza en `p = 2` e intenta verificar si es divisible por todos los valores de `d` menores a `p`.
- Si `p` es primo (es divisible solo por 1 y por sí mismo), lo imprime y aumenta el contador `c`.
- El bucle continúa hasta que has encontrado `n` números primos.
