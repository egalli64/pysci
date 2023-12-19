"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions

Aggregation and accumulation
"""
import numpy as np

a = np.arange(1, 7)

print(f"Reducing {a} on add gives", np.add.reduce(a))
print(f"Reducing {a} on divide gives", np.divide.reduce(a))

print(f"sum is {a.sum()} and prod is {a.prod()}")
print(f"min is {a.min()} at {a.argmin()}, max is {a.max()} at {a.argmax()}")
print(f"mean is {a.mean():.2f}, std dev {a.std():.2f}, variance {a.var():.2f}")

print(f"Cumulative sum on {a} is", np.add.accumulate(a))
print(f"Cumulative division on {a} is", np.divide.accumulate(a))
print(f"cumsum is {a.cumsum()}, cumprod is {a.cumprod()}")

m = np.random.random((2, 3))
print("A matrix:\n", m)
print(f"Sum:", m.sum())
print(f"Sum by column (collapsing rows, axis 0):", m.sum(axis=0))
print(f"Sum by row (collapsing columns, axis 1):", m.sum(axis=1))
print(f"Max by column:", m.max(axis=0))
print(f"Mean by row:", m.mean(axis=1))
print(m.cumsum(axis=0), "Cumulative sum by column")
print(m.cumsum(axis=1), "Cumulative sum by row")
