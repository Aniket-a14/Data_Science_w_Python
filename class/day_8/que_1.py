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