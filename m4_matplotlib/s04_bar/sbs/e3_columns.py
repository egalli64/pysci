"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple bar chart on pandas DataFrame columns (seaborn)
Requires iris.csv from https://github.com/mwaskom/seaborn-data
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris = pd.read_csv("data/iris.csv")
# by default the used estimator is the mean
sns.barplot(x="species", y="sepal_length", data=iris, errorbar=None)

plt.xlabel("Species")
plt.ylabel("Average Sepal Length")
plt.title("Average Sepal Length for Each Species (seaborn)")
plt.show()
