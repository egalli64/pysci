"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

split() on 2D array
"""

import numpy as np

m = np.arange(6).reshape((2, 3))
print(f"{m}: a two-dimension array shaped {m.shape}")

ms = np.split(m, 2, axis=0)
print("Vertical (axis 0) split in two equal parts:")
for i, xs in enumerate(ms):
    print(f"{i}: {xs}")

try:
    np.split(m, 3)
except ValueError as ex:
    print("A split in three parts causes a ValueError:", ex)
