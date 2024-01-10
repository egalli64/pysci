"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Reducing
"""
import numpy as np

a = np.arange(1, 7)

print(f"Reducing {a} by add() gives", np.add.reduce(a))
print(f"Reducing {a} by divide() gives", np.divide.reduce(a))

print(f"Sum is {a.sum()} and prod is {a.prod()}")
print(f"Min is {a.min()} at {a.argmin()}, max is {a.max()} at {a.argmax()}")
print(f"Mean is {a.mean():.2f}, std dev {a.std():.2f}, variance {a.var():.2f}")

print("\nIs _any_ element even?", np.any(a % 2 == 0))
print("Is _any_ element even (by reduce)?", np.logical_or.reduce(a % 2 == 0))
print("Are _all_ elements even?", np.all(a % 2 == 0))
print("Are _all_ elements even (by reduce)?", np.logical_and.reduce(a % 2 == 0))
print()

m = np.random.random((2, 3))
print(m, "a two dimension array")
print("Sum:", m.sum())
print("Sum by column (collapsing rows, axis 0):", m.sum(axis=0))
print("Sum by row (collapsing columns, axis 1):", m.sum(axis=1))
print("Max by column:", m.max(axis=0))
print("Mean by row:", m.mean(axis=1))
