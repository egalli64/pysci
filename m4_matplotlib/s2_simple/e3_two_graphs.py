"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw more line graphs in a figure
"""
import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(-2 * np.pi, 2 * np.pi, 200)

plt.plot(xs, np.sin(xs))
plt.plot(xs, (lambda x: x**2 - 20)(xs))
plt.show()
