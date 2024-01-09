"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple line graph - parabola
"""
import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(-5, 5, 100)
plt.plot(xs, (lambda x: x**2)(xs))
plt.show()
