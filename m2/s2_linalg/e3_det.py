"""
Python and Science

https://github.com/egalli64/pysci

Module 2 - SciPy

Linear Algebra - determinant
"""
import numpy as np
from scipy import linalg

a = np.array([[1, 2], [3, 4]])
det_a = linalg.det(a)
print(a, "the determinant is", det_a)
