"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Fancy Indices
"""

import numpy as np

a = np.random.randint(1, 11, size=6)
indices = [4, 2, 0, -1]
b = a[indices]

print(f"Using fancy indices {indices} on {a} to get {b}\n")

# the indices shape determines the resulting array shape
square_indices = [[4, 2], [0, -1]]
print(a[square_indices], "is the result when fancy indices are", square_indices)
print()

# fancy indices in more dimensions
a2 = a.reshape(2, 3)
print(a2, "array reshaped to", a2.shape)
rows = np.array([1, 1, 0, -1])
cols = np.array([0, 1, 0, -1])
print("Fancy indices for (i, j) on the matrix give:", a2[rows, cols])
print()

# Using fancy indices to write in an array
print("Change values by fancy indices:", a, end=" -> ")
a[indices] = 42
print(a)
