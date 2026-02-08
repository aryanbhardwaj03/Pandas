import pandas as pd

df = pd.read_csv("pokemon.csv")

df=df.drop(columns=["Legendary", "No"])

print(df)

df= df.dropna(subset=["Type2"])

print(df.to_string())

df = df.fillna({"Type2": "None"})
print(df.to_string())

# 3. Fix inconsistet values

df["Type1"]= df["Type1"].replace({"Grass":"GRASS", 
                                  "Fire":"FIRE",
                                  "Water":"WATER"})

print(df.to_string())


# 4 . Standardize text

df["Name"]=df["Name"].str.lower()

print(df.to_string())

# 5. Fix data type
df["Legendary"]= df["Legendary"].astype(bool)

print(df.to_string())