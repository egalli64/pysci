"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Slicing a 1D array
"""

import numpy as np

a = np.arange(10)
print("An array:", a)

# specifying start and end
print("Central part [3, 7):", a[3:7])

print("Head, till 3 (excluded):", a[:3])

tail = a[5:]
print("Tail, from 7:", a[7:])

# NumPy slices are views
tail[2] += 20
print("Changing a slice changes the original array:", a)

# explicit slice-copy
tail = a[-3:].copy()
print("Tail, last three elements (copy):", tail)

a[7] -= 20
print("Original array and slice-copy are indipendent object:", a, tail)
