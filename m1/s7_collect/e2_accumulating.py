"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Accumulating
"""
import numpy as np

a = np.arange(1, 7)

print(f"Cumulative sum on {a} is", np.add.accumulate(a))
print(f"Cumulative division on {a} is", np.divide.accumulate(a))
print(f"cumsum() gives {a.cumsum()}, cumprod gives {a.cumprod()}")

m = np.random.random((2, 3))
print(m, "a two dimension array")
print(m.cumsum(axis=0), "Cumulative sum by column")
print(m.cumsum(axis=1), "Cumulative sum by row")
