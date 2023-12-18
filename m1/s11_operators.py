"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Boolean operators
"""
import numpy as np

a = np.random.randint(1, 11, size=12)
print("a is", a)

# bitwise operators should be used
print("a in [3 .. 5]:", np.sum((a >= 3) & (a <= 5)))
print("a outside [3 .. 5] (or):", np.sum((a < 3) | (a > 5)))
print("a outside [3 .. 5] (not):", np.sum(~((a >= 3) & (a <= 5))))
# logical operators won't work
# print("a in [3 .. 5]:", np.sum((a >= 3) and (a <= 5)))
