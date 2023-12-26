"""
Python and Science

https://github.com/egalli64/pysci

Module 2 - SciPy

Linear Algebra - norm
"""
import numpy as np
from scipy import linalg

a = np.array([[1, 2], [3, 4]])
print(a, "Frobenius norm:", linalg.norm(a))
print("L1 norm", linalg.norm(a, 1))
