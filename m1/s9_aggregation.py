"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Aggregating function: folding, accumulating, ...
"""
import numpy as np

a = np.arange(1, 7)

print(f"Folding {a} on add gives", np.add.reduce(a))
print("Same, but by method sum()", a.sum())
print("prod()", a.prod())
print(f"Folding {a} on divide gives", np.divide.reduce(a))

print(f"Cumulative sum on {a} is", np.add.accumulate(a))
print("Same, but by method cumsum()", a.cumsum())
print("cumprod()", a.cumprod())
print(f"Cumulative division on {a} is", np.divide.accumulate(a))

print("Min and max:", a.min(), a.max())
print("Mean and standard deviation:", a.mean(), a.std())

m = np.random.random((2, 3))
print("A matrix:\n", m)
print(f"Sum:", m.sum())
print(f"Sum by column (collapsing rows, axis 0):", m.sum(axis=0))
print(f"Sum by row (collapsing columns, axis 1):", m.sum(axis=1))
print(f"Max by column:", m.max(axis=0))
print(f"Mean by row:", m.mean(axis=1))
