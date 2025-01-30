"""
Python and Science

https://github.com/egalli64/pysci

Module 2 - SciPy

Linear Algebra - determinant
"""

import numpy as np
from scipy import linalg as la

m = np.array([[1, 2], [3, 4]])
det_m = la.det(m)
print(m, "the determinant is", det_m)

print("\nOne-dimensional array has no determinant, a ValueError is raised")
try:
    la.det(np.arange(3))
except ValueError as ex:
    print(ex)
