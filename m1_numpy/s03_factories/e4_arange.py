"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

ndarray factory arange()
"""

import numpy as np

print("*** array constructor + standard range")
print(np.array(range(2, 11, 2)))

print("*** using arange to get the same result")
print(np.arange(2, 11, 2))

print("*** arange works on floats too")
print(np.arange(1.0, 1.51, 0.1))
