"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array split
"""
import numpy as np

a = np.arange(1, 10)
print("An array", a)

a1, a2, a3 = np.split(a, [3, 6])
print("Split in three:", a1, a2, a3)

m = np.arange(16).reshape((4, 4))
print("A matrix:\n", m)

above, below = np.vsplit(m, [2])
print("Vertical split in two:")
print(above)
print(below)

left, right = np.hsplit(m, [2])
print("Horizontal split in two:")
print(left)
print(right)
