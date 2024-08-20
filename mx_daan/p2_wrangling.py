"""
Python and Science

https://github.com/egalli64/pysci

Module X - Data Analysis

Data wrangling
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from p1_read import load_cars

print("*** The dataset as loaded (plus column names)")
df = load_cars()
print(df.head(), "\n")

print("*** Replacing the '?' marker with NaN")
df.replace("?", np.NaN, inplace=True)
print(df.head(), "\n")

print("*** Null found in columns", end=" ")
cols_with_null = [col for col in df.columns if any(df[col].isnull())]
print(cols_with_null)

# convert each value in T/F checking null
df_null = df.isnull()
for col in cols_with_null:
    print(col, end=": ")
    print(df_null[col].value_counts().get(True))
print()

# mean
cols_to_avg = ["normalized-losses", "bore", "stroke", "horsepower", "peak-rpm"]
print("*** Replace by mean the missing values in", cols_to_avg)
for col in cols_to_avg:
    fix = round(df[col].astype("float").mean(axis=0), 2)
    print(f" in {col} is set to {fix}")
    df[col].replace(np.nan, fix, inplace=True)

# frequency
print()
print(df["num-of-doors"].value_counts())
fix = df["num-of-doors"].value_counts().idxmax()
print("*** Using the most common value:", fix)
df["num-of-doors"].replace(np.nan, fix, inplace=True)

# remove
print("*** No use here for rows with no price, remove them")
df.dropna(subset=["price"], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

# column types
print("*** Fix column types")
print(df.dtypes)

float_cols = ["bore", "stroke", "price", "peak-rpm"]
int_cols = [
    "symboling",
    "normalized-losses",
    "engine-size",
    "curb-weight",
    "horsepower",
    "city-mpg",
    "highway-mpg",
]

df[float_cols] = df[float_cols].astype("float")
df[int_cols] = df[int_cols].astype("int")

print("*** Fixed column types")
print(df.dtypes)

print("*** Add columns with standard format")
df["city-L/100km"] = 235 / df["city-mpg"]
df["highway-L/100km"] = 235 / df["highway-mpg"]

print(df[["city-L/100km", "highway-L/100km"]].head())
print()

normalized_cols = ["length", "width", "height"]
print("*** Normalize", normalized_cols)
# let them range in [0..1]
for col in normalized_cols:
    df[col] = df[col] / df[col].max()

print(df[normalized_cols].head())

# saving on disk
# df.to_csv("data/cars.csv")

# divide the HP interval in three bins
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
labels = ["Low", "Medium", "High"]

# cut the HP in the three groups
df["hp-bins"] = pd.cut(df["horsepower"], bins, labels=labels, include_lowest=True)

# raw histogram
# print(df[["horsepower", "hp-bins"]].head())
# print(df["hp-bins"].value_counts())

plt.hist(df["horsepower"])

# binned bar chart
# plt.bar(labels, df["hp-bins"].value_counts())

# histogram
# plt.hist(df["horsepower"], bins = 3)

# show it
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
plt.show()
