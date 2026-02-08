import pandas as pd

df = pd.read_csv("pokemon.csv")

# legendary_pokemon = df[df["Legendary"]== 1]
# print(legendary_pokemon)


# water_pokemon = df[(df["Type1"] == "Water") |
#                    (df["Type2"]=="Water")]

# print(water_pokemon)

ff_pokemon = df[df["Type1"]=="Fire" &
                (df["Type2"]== "Flying")]

print(ff_pokemon)
