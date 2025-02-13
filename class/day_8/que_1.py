import pandas as pd
import numpy as np

l=[12,25,56,88]
df= pd.DataFrame(l, columns=["Roll No"])
print(df,"\n")


#create a series from an array using pandas and numpy
data = np.array([90,75,50,66])
s = pd.Series(data)
print(s,"\n")


data = np.array(['a','b','c','d'])
s = pd.Series(data, index=[100,101,102,103])
print(s,"\n")
# we passed index to the series so to get a custom index column


data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print(s,"\n")


data = {'Aniket': 100, 'Ankit': 200, 'Raj': 300, 'Sayak': 400}
s = pd.Series(data, index=['Aniket', 'Ankit'])
print(s,"\n")


data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data, index=['b','c','d','a'])
print(s,"\n")


s = pd.Series(5, index=[100,101,102,103])
print(s,"\n")


d = {'one': pd.Series([1,2,3], index=['apple','ball','clock']),
     'two': pd.Series([11,22,33,44], index=['apple','ball','clock','doll'])}
df = pd.DataFrame(d)
print(df,"\n")
print(df[2:4],"\n")


df = pd.DataFrame([[1,2,3],[4,5,6]], columns=['a','b','c'])
df2 = pd.DataFrame([[7,8,9],[10,11,12]], columns=['a','b','c'])
df = df._append(df2)
print(df,"\n")
df = df.drop(0)
print(df,"\n")


