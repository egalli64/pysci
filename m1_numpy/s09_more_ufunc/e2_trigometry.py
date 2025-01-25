"""
Python and Science

https://github.com/egalli64/pysci

Module 1 - NumPy

More Universal Functions

Trigonometry
"""
import numpy as np

angles = np.linspace(0, np.pi, 3)
print("Angles:", angles)

print("sin:", np.sin(angles))
print("cos:", np.cos(angles))
print("tan:", np.tan(angles))

values = [-1, 0, 1]
print("values:", values)
print("arcsin:", np.arcsin(values) / np.pi)
print("arccos:", np.arccos(values) / np.pi)
print("arctan:", np.arctan(values) / np.pi)
