"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

More Universal Functions

Solving a linear system
"""
import numpy as np
from numpy import linalg as la

v = np.array([1, 4])
print("Given the vector v =", v)
m = np.arange(1, 5).reshape(2, 2)
print(m, "and the matrix m")

x = la.solve(m, v)
print("The linear system mx = v has solution", x)

v2 = m @ x
print("As confirmation, m @ x is", v2)
print("Is v2 close enough to v?", np.allclose(v, v2))
