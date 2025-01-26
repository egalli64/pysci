"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Indexing on 1D array
"""

import numpy as np

throws = np.random.randint(1, 7, size=3)
print("Throws:", throws)
print(f"First throw is {throws[0]}, last one is {throws[-1]}")

# looping on all the indices in the ndarray
print("Looping on the throws indices", end=": ")
for i in range(throws.size):
    print(throws[i], end=" ")
print()

# ndarray is an iterable
print("Iterate on throws", end=": ")
for throw in throws:
    print(throw, end=" ")
print()
