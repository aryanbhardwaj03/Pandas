import pandas as pd
# print("Pandas Version:")
# print(pd.__version__)
# print("First Series:")
# data = [100 ,102,104,106,108]
# series=pd.Series(data)


# print(series)
# print("Second Series:")
# data1 = [100.1,1002.2,104.3,106.4]
# series = pd.Series(data1)
# print(series)


# print("Third Series:")
# data2 = ["A","B","C","D"]
# series2 = pd.Series(data2)
# print(series2)


# print("Fourth Series:")
# data3=[True,False,True]
# series3=pd.Series(data3)
# print(series3)


# data4=[100,102,104,106]
# series4=pd.Series(data4,index=["A","B","C","D"])
# print("Fourth Series :")
# print(series4)


# data5=[100,102,104,106]
# series5=pd.Series(data5,index=["# Apartment1:","# Apartment2:"," # Apartment3:"," # Apartment4:"])
# print("Fifth Series:")
# print(series5)

# data6 =[100,102,104]
# series6=pd.Series(data6,index=["A","B","C"])
# print("At particular index value:")
# series6.loc["C"]=200
# print(series6)

calories = {"Day 1": 1700 , "Day 2": 2000 , "Day 3": 1500}
series = pd.Series(calories)
print(series)
series.loc["Day 2"]+=1000
print(series)
print(series >=2000)
