"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array transposing
"""
import numpy as np

a = np.arange(12)
print(a, "an array shaped", a.shape)

at = a.T
print(f"{at}, a mono-dimensional transpose array is just an alias for the orginal array {at.shape}\n")

m = a.reshape(3, 4)
print(m, f"m is shaped {m.shape}")

mt = m.T
print(f"{mt}, the multi-dimensional transpose of m has shape {mt.shape}\n")
