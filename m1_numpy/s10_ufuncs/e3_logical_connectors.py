"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Logical connectors
"""
import numpy as np

xs = np.random.randint(1, 11, size=6)
print("xs is", xs)

# bitwise operators should be used
print("How many elements in xs are in [3 .. 5] (AND)?", np.sum((xs >= 3) & (xs <= 5)))
print("... and less than 3 or greater than 5 (OR)?", np.sum((xs < 3) | (xs > 5)))
print("... and _not_ in [3 .. 5] (NOT AND)?", np.sum(~((xs >= 3) & (xs <= 5))))

try:
    # logical operators won't work
    np.sum((xs >= 3) and (xs <= 5))
except ValueError as ex:
    print("The exception message is misleading, use bitwise operators -", ex)
