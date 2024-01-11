"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple heat map from DataFrame columns
Requires tips.csv from https://github.com/mwaskom/seaborn-data
"""
import matplotlib.pyplot as plt
import pandas as pd

tips = pd.read_csv("data/tips.csv")
data = tips.pivot_table(index="day", columns="smoker", values="tip", aggfunc="mean")
plt.imshow(data)

plt.colorbar()
plt.xlabel("Smoker")
plt.ylabel("Day")
plt.title("Heatmap for Tips")
plt.xticks(range(len(data.columns)), data.columns)
plt.yticks(range(len(data.index)), data.index)
plt.show()
