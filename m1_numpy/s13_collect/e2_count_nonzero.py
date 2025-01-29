"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Reducing - count_nonzero()
"""

import numpy as np

a = np.array([0, 1, 3, 0, 3, 3])

print("The array:", a)
print("How many non-zero elements (sum() of booleans)?", np.sum(a != 0))
print("How many non-zero elements (count_nonzero())?", np.count_nonzero(a))
