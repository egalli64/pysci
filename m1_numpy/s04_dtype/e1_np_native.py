"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Native types
"""

import numpy as np

# boolean
xs = np.array([0, 27, -23], dtype=np.bool_)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

# integers
xs = np.array([-128, 127], dtype=np.int8)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

xs = np.array([0, 255], dtype=np.uint8)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

xs = np.array([-32_768, 32_767], dtype=np.int16)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

xs = np.array([-2_147_483_648, 2_147_483_647], dtype=np.int32)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

xs = np.array([-9_223_372_036_854_775_808, 9_223_372_036_854_775_807], dtype=np.int64)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

# real numbers
xs = np.array([-1, 0, 1], dtype=np.float16)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

xs = np.array([-1, 0, 1], dtype=np.float32)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

xs = np.array([-1, 0, 1], dtype=np.float64)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

# np.float128 could be not supported on a given platform
try:
    xs = np.array([-1, 0, 1], dtype=np.float128)
    print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)
except AttributeError as ex:
    print(ex)

# complex numbers
xs = np.array([-1, 0, 1], dtype=np.complex64)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

xs = np.array([-1, 0, 1], dtype=np.complex128)
print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)

# np.complex256 could be not supported on a given platform
try:
    xs = np.array([-1, 0, 1], dtype=np.complex256)
    print(f"A {xs.dtype} array ({xs.dtype.itemsize} byte):", xs)
except AttributeError as ex:
    print(ex)
