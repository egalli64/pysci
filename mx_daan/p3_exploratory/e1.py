"""
Python and Science

https://github.com/egalli64/pysci

Module X - Data Analysis

Exploratory Data Analysis - Descriptive Statistics
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("*** The dataset as loaded (plus column names)")
df = pd.read_csv("data/cars.csv")
print(df.head(), "\n")

print("\nCheck basic dataset description (NaN are skipped)")
print(df.describe())

print("\nDescribe objects")
print(df.describe(include=["object"]))

print("\nSummarizing categorical data by value_counts():")
wd_counts = df["drive-wheels"].value_counts()
print(wd_counts)

print("\nSame, but on data frame:")
wd_counts = df["drive-wheels"].value_counts().to_frame()
wd_counts.rename(columns={"drive-wheels": "value_counts"}, inplace=True)
print(wd_counts)

print("\nAnother example:")
engine_loc_counts = df["engine-location"].value_counts().to_frame()
engine_loc_counts.rename(columns={"engine-location": "value_counts"}, inplace=True)
engine_loc_counts.index.name = "engine-location"
print(engine_loc_counts)
