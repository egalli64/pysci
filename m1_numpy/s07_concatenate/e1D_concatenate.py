"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array - concatenate()
"""

import numpy as np

a1 = np.arange(3)
a2 = np.arange(3, 6)
print("Two arrays:", a1, a2)

# from two arrays to a new, joined, array
ac = np.concatenate((a1, a2))
print("Array concatenation:", ac)

# concatenate() on array-like objects
print("Concatenating a list and a tuple:", np.concatenate(([2, 4, 7], (8, 11, 23))))
