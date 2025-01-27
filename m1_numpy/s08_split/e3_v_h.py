"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

split() on 2D array, vsplit() and hsplit()
"""

import numpy as np

m = np.arange(6).reshape((2, 3))
print(f"{m}: a two-dimension array shaped {m.shape}")

ms = np.vsplit(m, 2)
print("vsplit in two equal parts:")
for i, xs in enumerate(ms):
    print(f"{i}: {xs}")

ms = np.hsplit(m, 3)
print("\nhsplit in two equal parts:")
for i, xs in enumerate(ms):
    print(f"{xs}: {i}")
