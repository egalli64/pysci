"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array slicing on N dimensional arrays
"""

import numpy as np

m = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]])
print(f"A two dimensional array:\n{m}\n")

# Slicing passing a range for each dimension
top_left = m[:2, :3]
print(f"Slicing the first two rows and first three columns:\n {top_left}\n")

# Changing in the slide and see the change in the original array too
top_left[0, 1] += 40
print(f"Slice {m[0]} is a view of the original array {top_left[0]}\n")

# Slice-copy
bottom_right = m[-2:, -2:].copy()
m[2, -2] += 10
print(f"Slice-copy, last two rows, last two columns:\n{bottom_right}")
# Original and slice are two different object
print(f"The original has changed! {m[2]}\n")

print(m[:, ::2], "slice, all rows, alternate columns\n")
print(m[::-1, ::-1], "slice, revert rows and columns\n")
print(m[-1, :], "last row")
print(m[0], "first row (simplified syntax)")
print(m[:, -1], "last column")
