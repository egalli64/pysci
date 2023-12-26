"""
Python and Science

https://github.com/egalli64/pysci

Module 2 - SciPy

Interpolation - 1-D - numpy.interp
"""
import numpy as np

x = np.linspace(0, 10, num=11)
y = np.cos(-(x**2) / 9.0)

print("The passed points:")
for p in zip(x, y):
    print(p)
print()

x_in = np.linspace(0, 10, num=1001)
y_in = np.interp(x_in, x, y)

print("Some interpolate points:")
for i in range(50, 1001, 100):
    print((x_in[i], y_in[i]))
