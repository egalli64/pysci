"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

More Universal Functions

Dot
"""
import numpy as np

a = np.arange(1, 4)
b = np.arange(2, -1, -1)
print(f"Two arrays: a is {a}, b is {b}\n")

print("Scalar product: a @ b =", a @ b)
print("Scalar product using function dot() on a and b:", np.dot(a, b))
