"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array split
"""
import numpy as np

a = np.arange(9)
print("An array", a)

print("The array split in 3:", np.split(a, 3))
print("Split at 2 and 7:", np.split(a, (2, 7)))

m = np.arange(16).reshape((4, 4))
print("A matrix:\n", m)

above, below = np.split(m, 2, axis=0)
print("Vertical split in two (axis 0):")
print(above, "is above")
print(below, "is below")

above, below = np.vsplit(m, 2)
print("Vertical split in two (vsplit):")
print(above, "is above")
print(below, "is below")

left, right = np.hsplit(m, 2)
print("Horizontal split in two (hsplit):")
print(left, "is left")
print(right, "is right")
