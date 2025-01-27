"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions: add() and subtract()
"""

import numpy as np

a = np.arange(1, 7)
b = np.random.randint(1, 10, size=6)
print("The arrays a and b are", a, b)

print("a + b:", a + b)
print("add() on a and b:", np.add(a, b))

print("a - b:", a - b)
print("subtract() on a and b:", np.subtract(a, b))
