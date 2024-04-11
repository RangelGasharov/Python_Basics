import pandas as pd


def read_csv(path):
    df = pd.read_csv(path, sep=",")
    print(df.head())
    print(df.tail())
    print(df.info())


read_csv("data.csv")
