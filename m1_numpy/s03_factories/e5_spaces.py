"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

ndarray factories linspace() and logspace()
"""

import numpy as np
import math

print("*** linear space, 5 values in [2, 10]")
print(np.linspace(2, 10, 5))

print("*** linear space, 5 integers in [2, 10]")
print(np.linspace(2, 10, 5, dtype=int))

print("*** linear space, 6 values in [1.0, 1.5]")
print(np.linspace(1.0, 1.5, 6))

print("*** logarithmic space, 3 values in [10**0, 10**2]")
print(np.logspace(0, 2, 3))

print("*** logarithmic space, 3 values in [e**0, e**1]")
print(np.logspace(0, 1, 3, base=math.e))
