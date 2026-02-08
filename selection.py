import pandas as pd

# SELECTION BY COLUMN 
df= pd.read_csv("pokemon.csv", index_col="Name")
# print(df["Name"])
# print(df["Name"].to_string())
# print(df.loc["Pikachu"])
# print(df.loc["Charizard":"Blastoise"])
# print(df.iloc[0:11:2, 0:3])

pokemon = input("Enter a Pokemon name:")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")
