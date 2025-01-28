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
print("a + 3:", a + 3)
print("add() on a and 3:", np.add(a, 3))
print()

print("a - b:", a - b)
print("3 - a:", 3 - a)
print("subtract() on a and b:", np.subtract(a, b))
print("subtract() on 3 and a:", np.subtract(3, a))
