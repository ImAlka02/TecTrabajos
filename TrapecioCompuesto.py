# Integración: Regla de los trapecios
# Usando una función fx()
import numpy as np
import math
import matplotlib.pyplot as plt

# INGRESO
fx = lambda x: math.exp(x)

# intervalo de integración
a = 0
b = 3
tramos = 4

# PROCEDIMIENTO
# Regla del Trapecio
# Usando tramos equidistantes en intervalo
h = (b-a)/tramos
xi = a
suma = fx(xi)
for i in range(0,tramos-1,1):
    xi = xi + h
    suma = suma + 2*fx(xi)
suma = suma + fx(b)
area = h*(suma/2)

# SALIDA
print('tramos: ', tramos)
print('Integral: ', area)