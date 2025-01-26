"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array reshaping
"""

import numpy as np

# 1D array, shaped (12,)
a = np.arange(12)
print(a, "an array shaped", a.shape)

# 2D array, shaped (3, 4), view on the original ndarray
m_3x4 = a.reshape(3, 4)
print(m_3x4, f"reshaped to {m_3x4.shape}")
print("Is the reshaped ndarray a copy?", m_3x4.base is None)

# all the elements should fit in the new shape
try:
    a.reshape(3, 3)
except ValueError as ex:
    print("If sizes are not matching, ValueError:", ex)

# add one dimension (row) by reshape()
row = a.reshape(1, 12)
print(row, "reshaped to", row.shape, "single row")
# add one dimension (row) by np.newaxis
row = a[np.newaxis, :]
print(row, "reshaped as single row by newaxis")

# add one dimension (column) by reshape()
column = a.reshape(12, 1)
print(column, "reshaped as single column matrix")
# add one dimension (column) by np.newaxis
column = a[:, np.newaxis]
print(column, "reshaped as single column by newaxis")
