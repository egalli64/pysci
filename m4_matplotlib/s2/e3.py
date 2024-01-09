"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple line graph with some info
"""
import matplotlib.pyplot as plt
import numpy as np

xs = [3, 7, 23]
ys = [5, 11, 5]

plt.plot(xs, ys)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Plotting a simple graph")
plt.show()
