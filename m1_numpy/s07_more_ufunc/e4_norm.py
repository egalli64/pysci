"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

More Universal Functions

Norm
"""
import numpy as np
from numpy import linalg as la

a = np.arange(1, 4)
print(f"The array a is {a}\n")

print("Vector 2-norm (default) for a is", la.norm(a))
print("Vector 1-norm for a is", la.norm(a, ord=1))
