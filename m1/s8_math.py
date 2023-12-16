"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Trigonometry, exponential and logarithmic functions
"""
import numpy as np

angles = np.linspace(0, np.pi, 3)
print("Angles:", angles)

print("sin:", np.sin(angles))
print("cos:", np.cos(angles))
print("tan:", np.tan(angles))

values = [-1, 0, 1]
print("values:", values)
print("arcsin:", np.arcsin(values) / np.pi)
print("arccos:", np.arccos(values) / np.pi)
print("arctan:", np.arctan(values) / np.pi)

xs = np.arange(1, 5)
print("xs", xs)

print("e^x", np.exp(xs), np.e**xs)
print("2^x", np.exp2(xs), 2**xs, np.power(2, xs))

xs = np.append(xs, [10, 100])
print("xs", xs)

print("ln", np.log(xs))
print("log2", np.log2(xs))
print("log10", np.log10(xs))
