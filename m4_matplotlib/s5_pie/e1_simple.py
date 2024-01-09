"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

Draw a simple pie chart
"""
import matplotlib.pyplot as plt

players = ["tom", "bob", "kim"]
scores = [12, 21, 18]

plt.pie(scores, labels=players, autopct="%.2f%%")
plt.title("A Pie Chart")
plt.show()
