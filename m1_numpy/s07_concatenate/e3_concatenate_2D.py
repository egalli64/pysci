"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

concatenate() on 2D arrays
"""

import numpy as np

m = np.random.randint(6, size=(2, 2))
print(f"{m}: a 2D array, shape {m.shape}")

row = np.random.randint(6, size=(1, 2))
print(f"{row}: a row, shaped {row.shape}")

col = np.random.randint(6, size=(3, 1))
print(f"{col}: a column, shaped {col.shape}")

print("Vertically concatenate the matrix with the row:")
mv = np.concatenate((m, row), axis=0)
print(f"{mv}: shaped {mv.shape}")

print("Horizontally concatenate the matrix with the column:")
mh = np.concatenate((mv, col), axis=1)
print(f"{mh}: shaped {mh.shape}")
