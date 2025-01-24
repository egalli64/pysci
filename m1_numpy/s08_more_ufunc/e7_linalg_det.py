"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

linalg - determinant
"""
import numpy as np
from numpy import linalg as la

a = np.array([[1, 2], [3, 4]])
det_a = la.det(a)
print(a, "the determinant is", det_a)

print("\nOne-dimensional array has no determinant, a LinAlgError is raised")
try:
    la.det(np.arange(3))
except la.LinAlgError as ex:
    print(ex)
