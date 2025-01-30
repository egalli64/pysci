"""
Python and Science

https://github.com/egalli64/pysci

Module 2 - SciPy

Linear Algebra - inverse
"""

import numpy as np
from scipy import linalg as la

m = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
print(m, "is m\n")

inv_m = la.inv(m)
print(inv_m, "is m inverse\n")

# proof that it works
m_id = m @ inv_m
print(m_id, "is m @ inv(m)\n")
print("Is m @ inv(m) close to the identity matrix?", np.allclose(m_id, np.eye(3)))
