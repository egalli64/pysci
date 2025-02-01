"""
Python and Science

https://github.com/egalli64/pysci

Module X - Data Analysis

Read data
"""
import pandas as pd

# remote access
# url =  "http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

# or, locally stored
url = "data/imports-85.csv"

# the dataset has no header, provide it by hand
headers = [
    "symboling",
    "normalized-losses",
    "make",
    "fuel-type",
    "aspiration",
    "num-of-doors",
    "body-style",
    "drive-wheels",
    "engine-location",
    "wheel-base",
    "length",
    "width",
    "height",
    "curb-weight",
    "engine-type",
    "num-of-cylinders",
    "engine-size",
    "fuel-system",
    "bore",
    "stroke",
    "compression-ratio",
    "horsepower",
    "peak-rpm",
    "city-mpg",
    "highway-mpg",
    "price",
]


def load_cars():
    """
    Load the cars dataset and give proper names to the columns

    Return the generated dataframe
    """
    df = pd.read_csv(url, header=None)
    df.columns = headers
    return df


if __name__ == "__main__":
    df = load_cars()

    print("Columns are named:", df.columns)

    print("\nFirst three rows in the dataset are ...")
    print(df.head(3))
    print("... and the last five ones are ...")
    print(df.tail())

    # ---------------------
    print("\ncheck column data types")
    print(df.dtypes)

    print("\ncheck description for all columns")
    print(df.describe(include="all"))

    print("\ncheck description for given columns")
    print(df[["length", "width"]].describe())

    print("\ncheck info")
    df.info()

    # -----------------

    # remove rows where the price is not available
    df = df.dropna(subset=["price"], axis=0)
    print(df.head(20))

    # saving a local copy
    # df.to_csv("data/cars.csv")
