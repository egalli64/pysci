"""
Python and Science

https://github.com/egalli64/pysci

Module 2 - SciPy

Integration - quad
"""

from scipy import integrate


def parabola(x):
    return x**2


interval = (0, 1)
result = integrate.quad(parabola, *interval)
print("Result and error estimation:", result)
