"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Fancy Indices
"""
import numpy as np

a = np.random.randint(1, 11, size=12)
print("a is", a)

# single indexing
print("a[-1] is", a[-1])

# slicing
print("a[3:-3] is", a[3:-3])

# masking
print("a[a % 2 == 0] is", a[a % 2 == 0])

# single indexing + new array
b = [a[3], a[5], a[0], a[-1]]
print("new array by copy of elements in position 3, 5, 0, -1:", b)
# same, by fancy indices
indices = [3, 5, 0, -1]
c = a[indices]
print("Same, fancy indices:", c)

# the indices determine the resulting array shape
square_indices = np.array([[3, 5], [0, -1]])
print("Indexing against:\n", square_indices)
print("Result is:\n", a[square_indices])

# fancy indices in more dimensions
a2 = a.reshape(4, 3)
print("a2 is:\n", a2)
rows = np.array([1, 1, 0, -1])
cols = np.array([0, 2, 0, -1])
print("Result is:", a2[rows, cols])

# change values in array by fancy indices
print("before:", a)
a[indices] = 42
print("after:", a)
