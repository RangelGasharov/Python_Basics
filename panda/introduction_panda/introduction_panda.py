import pandas as pd
import sys

print(sys.version)
print("pandas version", pd.__version__)

df = pd.read_csv("pokemon_data.csv")

print(df.columns, "\n")
print(df[["Name", "Type 1", "HP"]][0:5], "\n")
print(df.head(3), "\n")
print(df.iloc[1:4], "\n")
print(df.iloc[2, 1], "\n")

for index, row in df.iterrows():
    print(index, row["Name"])

print(df.loc[df["Type 1"] == "Fire"], "\n")
print(df.describe(), "\n")
print(df.sort_values(["Name", "Type 1"], ascending=[True, False]), "\n")

df["Total"] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"]
print(df.head(5), "\n")
