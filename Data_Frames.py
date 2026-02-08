# DATA FRAMES

import pandas as pd 

data  = {"Name": ["Spongebob", "Alice", "John"]
         ,"Age": [30,35,40]}
df=pd.DataFrame(data, index=["Employee1", "Employee2", "Employee3"])
print(df)
print("________________")
print(df.loc["Employee2"])
df["Job"]=["Cook","N/A","Manager"]
print(df)
df["Job"]=["Cook","Engineer","Manager"]

# Add a new row
print("_________________________________________________")

new_row = pd.DataFrame([{"Name": "Sandy","Age":28,"Job":"Engineer"}],
                      index=["Employee4"])
df=pd.concat([df,new_row])
print(df)