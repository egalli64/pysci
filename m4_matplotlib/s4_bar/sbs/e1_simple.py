"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple bar chart (seaborn)
"""
import matplotlib.pyplot as plt
import seaborn as sns

players = ["tom", "bob", "kim"]
scores = [12, 21, 18]

sns.barplot(x=players, y=scores)

plt.xlabel("Player")
plt.ylabel("Score")
plt.title("A Bar Chart")
plt.show()
