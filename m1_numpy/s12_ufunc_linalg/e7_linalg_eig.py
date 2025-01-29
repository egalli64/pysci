"""
Python and Science

https://github.com/egalli64/pysci

Linear algebra

linalg - eigen values and vectors
"""

import numpy as np
from numpy import linalg as la

m = np.array([[4, -2], [1, 1]])
print(f"{m}: a squared matrix")

eigenvalues, eigenvectors = np.linalg.eig(m)
print(f"\n{eigenvalues}: eigenvalues")
print(f"{eigenvectors}: eigenvectors")
