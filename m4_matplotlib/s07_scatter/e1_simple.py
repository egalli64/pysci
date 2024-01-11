"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple scatter plot
"""
import matplotlib.pyplot as plt
import numpy as np

xs = np.random.rand(50)
ys = xs + np.random.rand(50)

# Create a scatter plot
plt.scatter(xs, ys)
plt.title("A Scatter Plot")
plt.show()
