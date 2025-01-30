"""
Python and Science

https://github.com/egalli64/pysci

Module 2 - SciPy

Interpolation - 1-D - Cubic spline
"""

import numpy as np
from scipy.interpolate import CubicSpline

xs = [1, 2, 3, 4, 5, 6]
ys = [1, 4, 8, 16, 25, 36]

print("The passed points:")
for p in zip(xs, ys):
    print(f"({p[0]}, {p[1]})")

c_spline = CubicSpline(xs, ys)

print(c_spline(2.5))

print("\nSome interpolate points:")
for x in np.arange(1.5, 6):
    print(f"({x}, {c_spline(x):.2f})")
