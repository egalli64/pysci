"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

More Universal Functions

Exponential, logarithmic
"""
import numpy as np

xs = np.arange(1, 5)
ys = np.arange(4, 0, -1)
print(f"xs is {xs} and ys is {ys}")

print("x ** y:", xs**ys, np.power(xs, ys))
print("2 ** xs:", 2**xs, np.power(2, xs))

print("e^x:", np.exp(xs), np.e**xs)
print("2^x:", np.exp2(xs), 2**xs, np.power(2, xs))

xs = np.append(xs, (10, 100))
print("now xs is", xs)

print("ln x:", np.log(xs))
print("log2 x:", np.log2(xs))
print("log10 x:", np.log10(xs))
