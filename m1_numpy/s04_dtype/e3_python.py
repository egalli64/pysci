"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Python types
"""

import numpy as np

xs = np.array([0, 27, -23], dtype=bool)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

xs = np.array([0, 27, -23], dtype=int)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

xs = np.array([0, 27, -23], dtype=float)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

xs = np.array([0, 27, -23], dtype=complex)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)
