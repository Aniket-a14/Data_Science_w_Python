import pandas as pd

d= {'one': pd.Series([1,2,3], index=['a','b','c']),
    'two': pd.Series([1,2,3,4], index=['a','b','c','d'])}

df= pd.DataFrame(d)
print(df.loc['b'])
print(df.iloc[2])
print(df[2:4])

df = pd.DataFrame([[1,2, "Aniket"],[3,4, "Ankit"]], columns=['a','b', 'c'])
df2 = pd.DataFrame([[5,"ok", "Raj"],[7,8, "Sayak"]], columns=['a','b', 'c'])
df= df._append(df2)
print(df)

df= df.drop(0)
print(df)