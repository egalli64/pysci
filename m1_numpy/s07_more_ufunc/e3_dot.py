"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

More Universal Functions

Dot
"""
import numpy as np

a = np.arange(1, 5)
b = np.arange(3, -1, -1)
print(f"Two arrays: a is {a}, b is {b}\n")

print("Scalar product: a @ b =", a @ b)
print("Same, using function dot() on a and b:", np.dot(a, b))
print()

c = np.array([3, 4])
print("The array c:", c)
m = a.reshape(2, 2)
print(m, "m, a two-dimensional array\n")

print("Matrix-vector product: m @ c =", m @ c)
print("Same, using function dot() on m and c:", np.dot(m, c))
print()

n = b.reshape(2, 2)
print(n, "n, another two-dimensional array\n")

print("Matrix-matrix product: m @ n =\n", m @ n)
print("Same, using function dot() on m and n:\n", np.dot(m, n))
