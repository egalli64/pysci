"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Unary universal Functions: - and absolute
"""

import numpy as np

m = np.arange(-2, 2).reshape((2, 2))
print(m, ": matrix m")

print("\nUnary minus")
print(-m, ": -m")
print(np.negative(m), "explicit call to negative()")

print("\nAbsolute")
print(np.abs(m), "np.abs()")
print(np.absolute(m), "np.absolute()")
print(abs(m), "built-in abs()")
