"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Reducing - on 1D array
"""

import numpy as np

a = np.arange(1, 7)

print(f"On {a} add.reduce(): {np.add.reduce(a)}, divide.reduce():", np.divide.reduce(a))

print(f"sum() gives {a.sum()} and prod() gives {a.prod()}")
print(f"min() gives {a.min()} at index {a.argmin()} (argmin())")
print(f"max() gives {a.max()} at index {a.argmax()} (argmax())")
print(f"mean() gives {a.mean():.2f}, std() {a.std():.2f}, var() {a.var():.2f}")

print("\nIs there _any_ even element (ufunc)?", np.any(a % 2 == 0))
print("Is there _any_ even element (array method)?", (a % 2 == 0).any())
print("Is _any_ element even (reduce)?", np.logical_or.reduce(a % 2 == 0))
print("Are _all_ elements even (ufunc)?", np.all(a % 2 == 0))
print("Are _all_ elements even (array method)?", (a % 2 == 0).all())
print("Are _all_ elements even (reduce)?", np.logical_and.reduce(a % 2 == 0))
