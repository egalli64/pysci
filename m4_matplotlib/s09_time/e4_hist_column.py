"""
Python and Science

https://github.com/egalli64/pysci

Module 4 - Matplotlib

A simple histogram with dates from a DataFrame column
Requires taxis.csv from https://github.com/mwaskom/seaborn-data
"""
import matplotlib.pyplot as plt
import pandas as pd

taxis = pd.read_csv("data/taxis.csv")
# convert datetime to date
taxis["dropoff"] = pd.to_datetime(taxis["dropoff"])
taxis["dropoff"] = taxis["dropoff"].dt.date

# a bin for each day
days = (taxis["dropoff"].max() - taxis["dropoff"].min()).days

plt.figure(figsize=(12, 6))
plt.hist(taxis["dropoff"], bins=days + 1, edgecolor="black")
plt.title("Histogram on Dates for Taxi Trips")
plt.show()
