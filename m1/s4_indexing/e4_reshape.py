"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array reshaping
"""
import numpy as np

a = np.arange(12)
print(a, "an array shaped", a.shape)

m = a.reshape(3, 4)
print(m, f"reshaped to {m.shape}")

a[-2] *= 2
print(m[-1], "reshaping generate a view (whenever possible)")

try:
    a.reshape(3, 3)
except ValueError as ex:
    print("If sizes are not matching, ValueError:", ex)

row = a.reshape(1, 12)
print(row, "reshaped to", row.shape, "single row")
row_2 = a[np.newaxis, :]
print(row_2, "reshaped as single row by newaxis")

column = a.reshape(12, 1)
print(column, "reshaped as single column matrix")
column_2 = a[:, np.newaxis]
print(column_2, "reshaped as single column by newaxis")
