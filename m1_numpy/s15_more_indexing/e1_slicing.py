"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Indexing - plain and by slicing
"""

import numpy as np

a = np.random.randint(1, 11, size=6)
print("a is", a)

# plain, single indexing
print("a[-1] is", a[-1])

# slicing
print("a[2:-2] is", a[2:-2])

# single indexing + new array
b = np.array([a[3], a[5], a[0], a[-1]])
print("creating a new array by copy of single elements is clumsy:", b)
