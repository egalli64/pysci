"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Folding and accumulating
"""
import numpy as np

a = np.arange(1, 7)

print(f"Folding {a} on add gives", np.add.reduce(a))
print("Same, but using sum()", np.sum(a))
print("prod()", np.prod(a))
print(f"Folding {a} on divide gives", np.divide.reduce(a))

print(f"Cumulative sum on {a} is", np.add.accumulate(a))
print("Same, but using cumsum()", np.cumsum(a))
print("cumprod()", np.cumprod(a))
print(f"Cumulative division on {a} is", np.divide.accumulate(a))
