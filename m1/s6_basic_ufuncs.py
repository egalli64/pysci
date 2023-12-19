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
print("a + 3:", a + 3, np.add(a, 3))
print("a + b:", a + b, np.add(a, b))

print("a - 3:", a - 3, np.subtract(a, 3))
print("3 - a:", 3 - a, np.subtract(3, a))
print("a - b:", a - b, np.subtract(a, b))

print("2 * a:", 2 * a, np.multiply(2, a))

print("a / 2:", a / 2, np.divide(a, 2))
print("2 / a:", 2 / a, np.divide(2, a))
print("a / b:", a / b)

print("a // 2:", a // 2, np.floor_divide(a, 2))
print("a % 2:", a % 2, np.mod(a, 2))
