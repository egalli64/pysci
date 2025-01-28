"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Unary universal Functions: - and absolute - result in out parameter
"""

import numpy as np

result = np.empty((2, 2), np.int_)
print(result, "buffer for result")

m = np.arange(-2, 2).reshape((2, 2))
print(m, ": matrix m")

print("\nUnary minus")
np.negative(m, out=result)
print(result)

print("\nAbsolute")
np.abs(m, out=result)
print(result, "np.abs()")

np.absolute(m, out=result)
print(result, "np.absolute()")
