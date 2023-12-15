"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array slicing - matrix
"""
import numpy as np

m = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]])
print("A matrix:\n", m)

top_left = m[:2, :3]
print("First two rows, first two columns:\n", top_left)

alt_col = m[:, ::2]
print("All rows, alternate columns:\n", alt_col)

full_reverse = m[::-1, ::-1]
print("Revert rows and columns:\n", full_reverse)

last_row = m[-1, :]
print("Last row:", last_row)

first_row = m[0]
print("First row (simplified syntax):", first_row)

last_col = m[:, -1]
print("Last column:", last_col)
