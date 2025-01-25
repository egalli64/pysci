"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Alias types
"""

import numpy as np

xs = np.array([-128, 127], dtype=np.int_)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

# np.float_ has been removed in NumPy 2.0 Use np.float64 instead
try:
    xs = np.array([-1, 0, 1], dtype=np.float_)
    print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)
except AttributeError as ex:
    print(ex)

# np.complex_ has been removed in NumPy 2.0. Use np.complex128 instead
try:
    xs = np.array([-1, 0, 1], dtype=np.complex_)
    print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)
except AttributeError as ex:
    print(ex)
