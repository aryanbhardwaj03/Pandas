import pandas as pd

# aggregate functions = Reduces a set of values into a single summary value
#                       Used to summarize and analyze data
#                       Often used with the groupby() function 

df= pd.read_csv("pokemon.csv")
# print(df.mean())
group = df.groupby("Type1")

print(group["Height"].mean())

