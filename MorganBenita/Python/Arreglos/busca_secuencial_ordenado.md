# Algoritmo 1.7: Busca_secuencial_ordenado

El algoritmo busca un elemento X en un arreglo unidimensional V de N elementos que se
encuentra ordenado crecientemente. POS indica la posición de X en Vo la posición en la que
estaria X
{I es una variable de tipo entero }
1. Hacer I = 1
2. Mientras (I <= N) y (V[I] < X) Repetir
Hacer I = I + 1
3. {Fin del ciclo del paso 2}
4. Si (I > N) o (V[I] > X)
entonces
Hacer POS = -I
si no
Hacer POS = I
5. {Fin del condicional del paso 4}