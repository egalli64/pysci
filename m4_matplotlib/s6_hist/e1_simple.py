"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple histogram
"""
import matplotlib.pyplot as plt
import numpy as np

sepal_length = np.random.normal(6, 1, 150)
plt.hist(sepal_length, edgecolor="black")

plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Histogram for an Iris Sepal Length simulation")
plt.show()
