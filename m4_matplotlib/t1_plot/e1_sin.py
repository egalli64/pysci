"""
Python and Science

https://github.com/egalli64/pysci

Module 3 - Matplotlib

Draw a first line graph
"""
import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(0, 2 * np.pi, 200)
ys = np.sin(xs)

plt.plot(xs, ys)
plt.show()
