import pandas as pd
import matplotlib.pyplot as plt


def read_csv(path):
    df = pd.read_csv(path, sep=",")
    print(df.head())
    print(df.tail())
    print(df.info())


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


# read_csv("data.csv")
# read_json("https://www.w3schools.com/python/pandas/data.js")
correlation()
