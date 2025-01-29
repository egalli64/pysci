"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Reducing - on 2D array
"""

import numpy as np

m = np.random.random((2, 3))
print(m, "a two dimension array\n")
print("Sum:", m.sum())
print("Sum by column (collapsing rows, axis 0):", m.sum(axis=0))
print("Sum by row (collapsing columns, axis 1):", m.sum(axis=1))
print("Max by column:", m.max(axis=0))
print("Mean by row:", m.mean(axis=1))
