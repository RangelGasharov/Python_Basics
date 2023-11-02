import pandas as pd
import sys
import re

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

df = df.drop(columns=["Total"])

print(df.head(5), "\n")

df["Total"] = df.iloc[:, 4:10].sum(axis=1)
print(df.head(5), "\n")

cols = list(df.columns.values)
print(cols, "\n")
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head(5), "\n")

# df.to_csv("modified.csv", index=False)
# df.to_excel("modified.xlsx", index=False)
# df.to_csv("modified.txt", index=False, sep="\t")

print((df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")]))
new_df = df.loc[((df["Type 1"] == "Fire") | (df["Type 1"] == "Water")) & ((df["HP"] > 50) & (df["Legendary"] == True))]
# new_df.to_csv("filtered_new_df_modified.csv", index=False)

print(df.loc[df["Name"].str.contains("Mega")])
print(df.loc[df["Type 1"].str.contains("fire|grass", flags=re.I, regex=True)])
print(df.loc[df["Name"].str.contains("^pi[a-z]*", flags=re.I, regex=True)])

df.loc[df["Type 1"] == "Fire", "Legendary"] = True
print(df)
df.loc[df["Total"] >= 500, ["Generation", "Legendary"]] = [0, True]
print(df)

df = pd.read_csv("pokemon_data.csv")
print(df.groupby(["Type 1"]).head(3).sort_values("Type 1"))
print(df.groupby(["Type 1"]).count())
