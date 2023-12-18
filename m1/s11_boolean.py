"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Boolean Logic
"""
import numpy as np

a = np.random.randint(1, 11, size=12)
print("a is", a)
print("a > 5:", a > 5)
print("a <= 3:", a <= 3)
print("a == 6:", a == 6)
print("a % 2 == 0:", a % 2 == 0)

m = a.reshape(3, 4)
print(m)
print("m != 6:\n", m != 1)

# Since True == 1 and False == 0:
print("Count a > 5:", np.count_nonzero(a > 5))
print("Count a <= 5:", np.count_nonzero(a <= 5))
print("How many even values in a?", np.sum(a % 2 == 0))
print("How many m < 5 in each column?", np.sum(m < 5, axis=0))
print("How many m < 5 in each row?", np.sum(m < 5, axis=1))

# any and all
print("Any value in a < 5?", np.any(a < 5))
print("All values in m >= 3?", np.all(m >= 3))
print("All values in m > 1 (by row)?", np.all(m > 1, axis=1))

# mask
print("Show a > 5", a[a > 5])
print("Show a <= 5", a[a <= 5])
