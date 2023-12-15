"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array concatenate
"""
import numpy as np

a1 = np.arange(3)
a2 = np.arange(3, 6)
print("Two arrays:", a1, a2)

ac = np.concatenate([a1, a2])
print("Concatenated:", ac)

m1 = np.array([[1, 2, 3], [3, 4, 5]])
m2 = np.array([[5, 6, 7], [7, 8, 9]])
print(f"Two matrices:\n{m1}\n{m2}")

# vertical concatenation
mv = np.concatenate([m1, m2])
print("Vertically concatenated:\n", mv)

mv2 = np.vstack([m1, m2])
print("Vertically stacked (same):\n", mv2)

mv3 = np.vstack([a1, m1])
print("Vertically stack a one-dimensional array and a matrix:\n", mv3)

# horizontal concatenation
mh = np.concatenate([m1, m2], axis=1)
print("Horizontally concatenated:\n", mh)

mh2 = np.hstack([m1, m2])
print("Horizontally stacked (same):\n", mh)

column = np.array([[7], [8]])
mh3 = np.hstack([m1, column])
print("Horizontally stack a one-column matrix and a 'normal' matrix:\n", mh3)
