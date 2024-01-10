"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple bar chart
"""
import matplotlib.pyplot as plt

players = ["tom", "bob", "kim"]
scores = [12, 21, 18]

plt.bar(players, scores)

plt.xlabel("Player")
plt.ylabel("Score")
plt.title("A Bar Chart")
plt.show()
