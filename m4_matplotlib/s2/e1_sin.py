"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple line graph - sine
"""
import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(0, 2 * np.pi, 200)
ys = np.sin(xs)

plt.plot(xs, ys)
plt.show()
