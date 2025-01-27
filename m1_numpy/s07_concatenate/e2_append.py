"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array - append()
"""

import numpy as np

a = np.arange(3)
print("An array:", a)

# append() a single value to an array (_not_ in-place!)
a2 = np.append(a, 21)
print("Append a single value:", a2)

a3 = np.append(a, (18, 27, 42))
print("Append a tuple:", a3)
