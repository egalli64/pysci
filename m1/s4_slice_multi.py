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

# NumPy slices are views
top_left[0, 1] += 40
print("Original and slices are all working on the same memory:", m[0])

bottom_right = m[-2:, -2:].copy()
print("Last two rows, last two columns (copy):\n", bottom_right)

m[2,-2] += 10
print("A copy is not affected by changes on the original:\n", bottom_right)

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
