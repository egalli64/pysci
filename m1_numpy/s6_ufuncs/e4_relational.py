"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Relational operators
"""
import numpy as np

a = np.random.randint(1, 11, size=12)
print("a is", a)
print("a > 5:", a > 5)
print("a <= 3:", a <= 3)
print("a == 6:", a == 6)
print("a % 2 == 0:", a % 2 == 0)
print()

m = a.reshape(3, 4)
print(m, "array a reshaped to", m.shape)
print(m != 1, "m != 1\n")

# Since True == 1 and False == 0:
print("Count a > 5:", np.count_nonzero(a > 5))
print("Count a <= 5:", np.count_nonzero(a <= 5))
print("Count even values in a by sum()", np.sum(a % 2 == 0))
print("Count m < 5 in each column by sum()", np.sum(m < 5, axis=0))
print("Count m < 5 in each row by sum()", np.sum(m < 5, axis=1))

print("\nMask to extract a copy of elements respecting a relation")
print("a > 5:", a[a > 5])
print("a <= 5:", a[a <= 5])
