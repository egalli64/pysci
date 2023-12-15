"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Types
"""
import numpy as np

a_bool = np.array([0, 27, -23], dtype=bool)
print(f"A {a_bool.dtype} array:", a_bool)

a_bool_np = np.array([0, 27, -23], dtype=np.bool_)
print(f"A {a_bool_np.dtype} array:", a_bool_np)

a_int = np.array([0, 27, -23], dtype=int)
print(f"A {a_int.dtype} array:", a_int)

a_int_np = np.array([0, 27, -23], dtype=np.int_)
print(f"A {a_int_np.dtype} array:", a_int_np)

a_int_8 = np.array([-128, 127], dtype=np.int8)
print(f"A {a_int_8.dtype} array:", a_int_8)

a_uint_8 = np.array([0, 255], dtype=np.uint8)
print(f"A {a_uint_8.dtype} array:", a_uint_8)

a_int_16 = np.array([-32_768, 32_767], dtype=np.int16)
print(f"A {a_int_16.dtype} array:", a_int_16)

# implicit dtype=np.int32
a_int_32 = np.array([-2_147_483_648, 2_147_483_647])
print(f"A {a_int_32.dtype} array:", a_int_32)

# implicit dtype=np.int64
a_int_64 = np.array([-9_223_372_036_854_775_808, 9_223_372_036_854_775_807])
print(f"A {a_int_64.dtype} array:", a_int_64)

a_float = np.array([0.42, 27, -23], dtype=float)
print(f"A {a_float.dtype} array:", a_float)

a_float_np = np.array([0.42, 27, -23], dtype=np.float_)
print(f"A {a_float.dtype} array:", a_float_np)

a_complex = np.array([0.42, 27, -23], dtype=complex)
print(f"A {a_complex.dtype} array:", a_complex)

a_complex_np = np.array([0.42, 27, -23], dtype=np.complex_)
print(f"A {a_complex.dtype} array:", a_complex_np)
