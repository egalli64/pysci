"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple heat map using seaborn
"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = np.random.rand(10, 10)
sns.heatmap(data, cmap="YlGnBu", annot=True, fmt=".1f", linewidths=1)

plt.title("A Heatmap")
plt.show()
