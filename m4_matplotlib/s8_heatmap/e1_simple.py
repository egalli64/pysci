"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple heat map (as plt image show)
"""
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)
plt.imshow(data)
plt.colorbar()

plt.title("A Heatmap")
plt.show()
