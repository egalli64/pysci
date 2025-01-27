"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array - vstack() and hstack()
"""

import numpy as np

m1 = np.arange(6).reshape(2, 3)
m2 = np.arange(6, 12).reshape(2, 3)
print(f"\nTwo dimensional arrays:\n{m1}\n{m2}")

# vertical concatenation
print("Stack them vertically ...")
print(np.vstack((m1, m2)))

# horizontal concatenation
print("Stack them horizontally ...")
print(np.hstack((m1, m2)))
