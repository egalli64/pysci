"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

split() on 2D array
"""

import numpy as np

m = np.arange(16).reshape((4, 4))
print(f"A two-dimension array shaped {m.shape}:\n", m)

above, below = np.split(m, 2, axis=0)
print("Vertical (axis 0) split in two equal parts:")
print(above, "is above")
print(below, "is below")

above, below = np.vsplit(m, 2)
print("vsplit in two equal parts:")
print(above, "is above")
print(below, "is below")

left, right = np.hsplit(m, 2)
print("\nhsplit in two equal parts:")
print(left, "is left")
print(right, "is right")
