"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions
"""
import numpy as np

a = np.arange(1, 7)
b = np.random.randint(1, 10, size=6)
c = np.random.randint(-2, 2, size=6)
print("The arrays a, b, and c are", a, b, c)
m = a.reshape((2, 3))
print(m, "is the matrix m\n")

# unary operations
print("-c:", -c, np.negative(c))
print(f"-m:\n", -m)

print("|c| is", np.abs(c), np.absolute(c), abs(c))

# binary operations
print("a + b:", a + b, np.add(a, b))
print("a - b:", a - b, np.subtract(a, b))
print("a * b:", a * b, np.multiply(a, b))
print("a / b:", a / b, np.divide(a, b))

print("a // b:", a // b, np.floor_divide(a, b))
print("a % b:", a % b, np.mod(a, b))
