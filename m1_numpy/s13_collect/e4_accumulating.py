"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Accumulating
"""

import numpy as np

a = np.arange(1, 7)

print(f"Passing {a} add.accumulate() gives", np.add.accumulate(a))
print(f" ... and divide.accumulate(a) gives", np.divide.accumulate(a))
print(f"Calling cumsum() on the array gives {a.cumsum()}")
print(f" ... and cumprod() gives {a.cumprod()}")
print()

m = np.random.random((2, 3))
print(m, "a two dimension array")
print(m.cumsum(axis=0), "Cumulative sum by column")
print(m.cumsum(axis=1), "Cumulative sum by row")
