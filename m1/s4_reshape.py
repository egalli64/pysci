"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array reshaping
"""
import numpy as np

a = np.arange(12)
print("An array:", a)

m = a.reshape(3, 4)
print("Reshaped as an array:\n", m)

a[-2] *= 2
print("Whenever possible, reshaping does not imply copying:", m[-1])

try:
    a.reshape(3, 3)
except ValueError as ex:
    print("If sizes are not matching, ValueError:", ex)

row = a.reshape(1,12)
print("Reshaping a one-dimensional array in a single-row matrix:", row)
row_2 = a[np.newaxis, :]
print("Same, by newaxis:", row_2)

column = a.reshape(12, 1)
print("Reshaping a one-dimensional array in a single-column matrix:\n", column)
column_2 = a[:, np.newaxis]
print("Same, by newaxis:\n", column_2)
