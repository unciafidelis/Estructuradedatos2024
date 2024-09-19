# Ejemplo 1.4
Sea CICLO un arreglo de 12 elementos reales con índices de tipo escalar o enumerados.

```python
import numpy as np

# Definir los meses como una lista
meses = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sept', 'oct', 'nov', 'dic']

# Cálculo de NTC usando la fórmula dada
NTC = (ord('dic') - ord('ene') + 1)  # Esto es incorrecto porque no se usa ord('dic') ni ord('ene')

# Inicializando NTC correctamente, debe ser 12 (de 'ene' a 'dic')
NTC = len(meses)

# Crear un arreglo de 12 elementos reales inicializados en 0.0
CICLO = np.zeros(NTC, dtype=float)

# Mostrar el arreglo inicial con valores predeterminados
print("Arreglo CICLO (valores iniciales para cada mes):")
for i, mes in enumerate(meses):
    print(f"CICLO[{mes}] hace referencia al elemento de la posición {mes} ({i + 1}ra.) = {CICLO[i]}")

# Ejemplos de acceso a valores utilizando los índices de los meses
print(f"\nCICLO['ene'] hace referencia al elemento de la posición ene: {CICLO[0]} (1ra.)")
print(f"CICLO['feb'] hace referencia al elemento de la posición feb: {CICLO[1]} (2da.)")
print(f"CICLO['dic'] hace referencia al elemento de la posición dic: {CICLO[11]} (12ava.)")
```