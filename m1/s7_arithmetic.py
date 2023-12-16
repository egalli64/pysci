"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

Universal Functions (Vectorized operations)

Arithmetic operators
"""
import numpy as np

a = np.arange(1, 7)
b = np.random.randint(1, 10, size=6)
print("The arrays a and b:", a, b)
m = a.reshape((2, 3))
print("The matrix m:\n", m)

print("-a:", -a, np.negative(a))
print(f"-m:\n", -m)

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
print("a ** 2:", a**2, np.power(a, 2))
print("2 ** a:", 2**a, np.power(2, a))
print("m ** 2\n", m**2)

c = np.random.randint(-2, 2, size=6)
print("c is", c)
print("|c| is", np.abs(c), np.absolute(c), abs(c))
