"""
Python and Science

https://github.com/egalli64/pysci

Module 2 - SciPy

Linear Algebra - inverse
"""
import numpy as np
from scipy import linalg

a = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
print(a, "is a\n")

inv_a = linalg.inv(a)
print(inv_a, "is a ^ -1 (inverse)\n")

# proof that it works
m_id = a @ inv_a
print(m_id, "is a @ a^-1\n")
print("Is a @ a^-1 close enough to the identity matrix?", np.allclose(m_id, np.eye(3)))
