"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Broadcasting
"""
import numpy as np

# adding two same sized arrays
a = np.arange(1, 4)
b = np.arange(6, 3, -1)
print(f"Adding a {a} and b {b} gives", a + b)

# broadcasting a scalar on a one-dimensional array
delta = 3
print(f"Adding a {a} and {delta} gives", a + delta)

# broadcasting a scalar on a two-dimensional array
eye_3 = np.eye(3, dtype=int)
print(f"Given eye_3, shaped {eye_3.shape}\n", eye_3)
print(f"Adding {delta} and eye_3 gives\n", eye_3 + delta)

# broadcasting an array on a two-dimensional array
print(f"Adding eye_3 and a {a} gives\n", eye_3 + a)
print(f"Same as adding a {a} and eye_3:\n", a + eye_3)

# broadcasting a column on a two-dimensional array
a_col = a.reshape(3, 1)
print("Given a column:\n", a_col)
print(f"Adding eye_3 and the column gives\n", eye_3 + a_col)

# broadcasting a row on a column
print(f"Adding b and the column gives\n", b + a_col)
