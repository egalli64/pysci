"""
Python and Science

https://github.com/egalli64/pysci

Module 2 - SciPy

Linear Algebra - solve a linear system
"""
import numpy as np
from scipy import linalg as la

a = np.array([[1, 2], [3, 4]])
b = np.array([[5], [6]])

print(a, "a\n", b, "b")
print("Solving a against b")
solution = la.solve(a, b)
print(solution)

# proof that it works
print("Is a @ solution equal to b?", np.all(a @ solution == b))
