"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Relational operators
"""

import numpy as np

a = np.random.randint(1, 7, size=10)
b = np.random.randint(1, 7, size=10)
print(f"a is {a}\nb is {b}\n")

print("a == 3:", a == 3)
print("a == b:", a == b)

print("a > 5:", np.greater(a, 5))
print("a <= b:", np.less_equal(a, b))
print("a % 2 == 0:", a % 2 == 0)
print()

m = a.reshape(2, 5)
print(m, "array a reshaped to m", m.shape)
print(m != 1, "m != 1\n")
