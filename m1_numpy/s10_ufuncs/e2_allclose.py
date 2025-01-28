"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

allclose()
"""

import numpy as np

a = np.array([1.000001, 2.000001, 3.000001])
b = np.array([1.000002, 2.000002, 3.000002])
print(f"a is {a}\nb is {b}")

print("Are close enough in all their elements?", np.allclose(a, b))

a = np.array([1.0001, 2.000001, 3.000001])
b = np.array([1.0002, 2.000002, 3.000002])
print(f"\na is {a}\nb is {b}")

print("Are close enough in all their elements?", np.allclose(a, b))
