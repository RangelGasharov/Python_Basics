import pandas as pd
import matplotlib.pyplot as plt


def read_csv(path):
    df = pd.read_csv(path, sep=",")
    print(df.head())
    print(df.tail())
    print(df.info())


def series():
    a = [1, 7, 2]
    # my_var = pd.Series(a)
    my_var = pd.Series(a, index=["x", "y", "z"])
    print(my_var)
    # print(my_var[0])
    print(my_var["y"])


def read_json(url):
    df = pd.read_json(url)
    print(df.head(10))
    print(df.tail(10))
    print(df.info())


def correlation():
    df = pd.read_csv("data.csv", sep=",")
    print(df.head())
    print(df.tail())
    print(df.info())
    print(df.corr())
    df.plot()
    plt.show()


def cleaning_data():
    df = pd.read_csv("dirtydata.csv", sep=",")
    df['Date'] = pd.to_datetime(df['Date'], format="mixed")
    df.dropna(subset=['Date'], inplace=True)

    print(df.head(10))
    print(df.tail(10))
    print(df.info())

    x = df["Calories"].mean()
    # df["Calories"].fillna(x, inplace=True)
    df.fillna({"Calories": x}, inplace=True)

    d = df["Duration"].mean()
    for x in df.index:
        if df.loc[x, "Duration"] > 2 * d:
            df.loc[x, "Duration"] = int(d)
    # df.dropna(inplace=True)

    # new_df = df.dropna()
    # print(new_df.info())

    print(df.info())


# read_csv("data.csv")
# read_json("https://www.w3schools.com/python/pandas/data.js")
# correlation()
# series()
cleaning_data()
