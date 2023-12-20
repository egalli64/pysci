"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Broadcasting 1D array
"""
import numpy as np

row = np.arange(1, 4).reshape(1, 3)
col = np.arange(6, 3, -1).reshape(3, 1)

print("Broadcasting a row onto a column")
print(f"{col} + {row} is ...\n{col + row}\n")

print("Broadcasting a row onto a 2D array")
eye = np.eye(3, dtype=int)
print(f"{eye} + {row} is ... \n{eye + row}\n")

m3d = np.ones((3, 2, 2), dtype=np.int_)
try:
    m3d + row
except ValueError as ex:
    print(f"Broadcasting a 1D array onto a 3D array leads to a ValueError: {ex}\n")
