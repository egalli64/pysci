"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

More Universal Functions

Linear combination
"""
import numpy as np

a = np.arange(1, 4)
b = np.arange(2, -1, -1)
print(f"Two arrays: a is {a}, b is {b}\n")

print("Scalar multiplication: 3*a =", 3 * a)
print("Scalar division: b/2 =", b / 2)
print("Linear combination: 3*a + b/2 =", 3 * a + b / 2)
