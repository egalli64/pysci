"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Boolean indexing / masking
"""

import numpy as np

a = np.random.randint(1, 11, size=6)
print("a is", a)

print("\nMask to extract a copy of elements respecting a relation")
print("a > 5:", a[a > 5])
print("a <= 5:", a[a <= 5])
print("a % 2 == 0:", a[a % 2 == 0])
