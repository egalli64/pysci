"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array slicing on N dimensional arrays
"""
import numpy as np

m = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]])
print(m, "is a two dimensional array")

top_left = m[:2, :3]
print(top_left, "slice, first two rows, first two columns")

# NumPy slices are views
top_left[0, 1] += 40
print(m[0], "changing a slice is same as changing the original array\n")

bottom_right = m[-2:, -2:].copy()
print(bottom_right, "slice (copy), last two rows, last two columns")

m[2,-2] += 10
print(bottom_right, "after creation, an array and its slice-copy are not related anymore\n")

alt_col = m[:, ::2]
print(alt_col, "slice, all rows, alternate columns\n")

full_reverse = m[::-1, ::-1]
print(full_reverse, "slice, revert rows and columns\n")

last_row = m[-1, :]
print(last_row, "last row")

first_row = m[0]
print(first_row, "first row (simplified syntax)")

last_col = m[:, -1]
print(last_col, "last column")
