"""
Python and Science

https://github.com/egalli64/pysci

Linear algebra

linalg - inverse
"""

import numpy as np
from numpy import linalg as la

m = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
print(m, "is m\n")

inv_m = la.inv(m)
print(inv_m, "is the m inverse\n")

# proof that it works
m_id = m @ inv_m
print(m_id, "is m @ inv(m)\n")
print("Is m @ inv(m) close to the identity matrix?", np.allclose(m_id, np.eye(3)))

print("\nOne-dimensional array has no inverse, LinAlgError is raised")
try:
    la.inv(np.arange(1, 5))
except la.LinAlgError as ex:
    print(ex)
