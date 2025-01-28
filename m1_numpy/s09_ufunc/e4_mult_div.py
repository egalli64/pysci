"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions: multiply(), divide(), floor_divide(), remainder(), mod()
"""

import numpy as np

# an array with 6 values in [-6 ... 6]
a = np.random.randint(-6, 7, size=6)
# an array with 6 values, 3 negatives, 3 positive (no zero)
b = np.concatenate((np.random.randint(-6, 0, size=3), np.random.randint(1, 7, size=3)))
print("The arrays a and b are", a, b)

print("a * b:", a * b)
print("3 * a:", 3 * a)
print("multiply() on a and b:", np.multiply(a, b))
print("multiply() on a and 3:", np.multiply(a, 3))

print("a / b:", a / b)
print("divide() on a and b:", np.divide(a, b))

print("a // b:", a // b)
print("floor_divide() on a and b:", np.floor_divide(a, b))

print("a % b:", a % b)
print("remainder() on a and b:", np.remainder(a, b))
# since NumPy 1.20 remainder() and mod() are synonyms
print("mod() on a and b:", np.mod(a, b))
