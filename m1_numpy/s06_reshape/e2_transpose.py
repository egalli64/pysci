"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Array transposing
"""

import numpy as np

# ndarray shaped (6,)
a = np.arange(6)
print(a, "an array shaped", a.shape)

# 1D array transpose is the array itself
print(f"{a.T}, a 1D transpose is just an alias for the orginal array {a.T.shape}\n")

# reshape to (1, 6), its transpose is (6, 1)
a2 = a[np.newaxis, :]
print(f"{a2} has shape {a2.shape}")
print(f"{a2.T} original array transposed to {a2.T.shape}\n")

# reshape to (2, 3), its transpose is (3, 2)
m = a.reshape(2, 3)
print(m, f"m is shaped {m.shape}")
print(f"{m.T} original array transposed to {m.T.shape}\n")
