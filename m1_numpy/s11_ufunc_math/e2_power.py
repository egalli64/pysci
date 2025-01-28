"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Math Universal Functions

power(), sqrt(), cbrt()
"""

import numpy as np

xs = np.arange(1, 5)
ys = np.arange(4, 0, -1)
print(f"xs is {xs} and ys is {ys}\n")

print("xs ** ys     :", xs**ys)
print("power(xs, ys):", np.power(xs, ys))
print("2 ** xs     :", 2**xs)
print("power(2, xs):", np.power(2, xs))
print()

print("sqrt(xs):", np.sqrt(xs))
print("cbrt(xs):", np.cbrt(xs))
