"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

String types
"""

import numpy as np

print("Unicode strings")

# preferred
xs = np.array([0, 27, -23], dtype=np.str_)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

# to force the fixed size
xs = np.array([0, 27, -23], dtype="U5")
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

# Python type
xs = np.array([0, 27, -23], dtype=str)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

print("\nByte strings")

# preferred
xs = np.array([0, 27, -23], dtype=np.bytes_)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

# to force the fixed size
xs = np.array([0, 27, -23], dtype="S5")
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

# Python type
xs = np.array([0, 27, -23], dtype=bytes)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)
