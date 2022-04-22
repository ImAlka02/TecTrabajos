import math
import numpy as np

def f(x):
    y = np.exp(x)
    return y

a = float(input("¿Cual es el limite inferior? \n"))
b = float(input("¿Cual es el limite superior? \n"))
n = int(input("¿Cual es el numero de intervalos? "))

x = np.zeros([n+1])
y = np.zeros([n])
z = np.zeros([n])

h = (b-a)/n

print (h)

x[0] = a
x[n] = b


suma1 = 0
suma2 = 0

for i in np.arange(1,n):
    x[i] = x[i-1] + h
    suma1 = suma1 + f(x[i])

alfa = (x[i]-x[i-1])/3

for i in np.arange(0,n):
    y[i] = (x[i-1]+ alfa)
    suma2 = suma2 + f(y[i])
    z[i] = y[i] + alfa


int3 = ((b-a)/(8*n)) * (f(x[0])+f(x[n]) + (3*(suma2+f(z[i]))) + (2*(suma1)))

print (int3)