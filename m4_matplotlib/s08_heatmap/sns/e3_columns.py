"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple heat map from DataFrame columns using seaborn
Requires tips.csv from https://github.com/mwaskom/seaborn-data
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

tips = pd.read_csv("data/tips.csv")
data = tips.pivot_table(index="day", columns="smoker", values="tip", aggfunc="mean")

sns.heatmap(data, cmap="YlGnBu", annot=True, fmt=".2f", linewidths=1)

plt.xlabel("Smoker")
plt.ylabel("Day")
plt.title("Heatmap for Tips (seaborn)")
plt.show()
