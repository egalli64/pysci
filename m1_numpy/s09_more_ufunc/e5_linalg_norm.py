"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

More Universal Functions

linalg - norm
"""
import numpy as np
from numpy import linalg as la

a = np.arange(1, 5)
print(f"The array a is {a}\n")

print("Vector 2-norm (default) for a is", la.norm(a))
print("Vector 1-norm for a is", la.norm(a, ord=1))
print()

m = a.reshape(2, 2)
print(m, "m, a two-dimensional array\n")
print("Matrix Forbenius norm ('fro' is the default) for m is", la.norm(m))
print("Matrix 1-norm for m is", la.norm(m, ord=1))
print("Matrix 2-norm for m is", la.norm(m, ord=2))
