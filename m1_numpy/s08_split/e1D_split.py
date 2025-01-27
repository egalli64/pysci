"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

split() on 1D array
"""

import numpy as np

a = np.arange(9)
print("An array", a)

# split in three equal subarray
print("A standard three-way split:", np.split(a, 3))

try:
    np.split(a, 2)
except ValueError as ex:
    print("A split in two parts causes a ValueError: ", ex)

# split in three subarray @ given index
print("A custom three-way split (at index 2 and 7):", np.split(a, (2, 7)))
