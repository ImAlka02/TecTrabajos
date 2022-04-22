# Integración: Regla Simpson 1/3
import numpy as np
import math
import matplotlib.pyplot as plt

# INGRESO:
fx = lambda x: math.exp(x)

# intervalo de integración
a = 0
b = 3
tramos = 2

# PROCEDIMIENTO
# Tarea: validar tramos par

# Regla de Simpson 1/3
h = (b-a)/tramos
xi = a
area = 0
for i in range(0,tramos,2):
    deltaA = (h/3)*(fx(xi)+4*fx(xi+h)+fx(xi+2*h))
    area = area + deltaA
    xi = xi + 2*h

# SALIDA
print('tramos:', tramos)
print('Integral: ', area)