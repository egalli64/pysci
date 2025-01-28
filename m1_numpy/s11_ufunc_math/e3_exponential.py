"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

More Universal Functions

Exponential
"""

import numpy as np

xs = np.arange(1, 5)
print(f"xs is {xs}\n")

print("e**xs  :", np.e**xs)
print("exp(xs):", np.exp(xs))
print()

print("2**xs       :", 2**xs)
print("exp2(xs)    :", np.exp2(xs))
print("power(2, xs):", np.power(2, xs))
