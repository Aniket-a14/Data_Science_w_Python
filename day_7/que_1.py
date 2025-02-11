import pandas as pd

a= pd.Series([1,2,3])
print(a)

b= pd.Series([1,2,3], index=['A','B','C'])
print(b)

data = {'a': 0.1, 'b': 1., 'c': '2.'}
s= pd.Series(data)
print(s)

data = {'a': 0.0, 'b': 1.0, 'c': '2.0'}
s1= pd.Series(data)
print(s1)

list = ['g','e','e','k','s']
s2 = pd.Series(list)
print(s2)

s3= pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
l= ['c','e']
print(s3['b'])
print(s3['e'])
print(s3[l])
print(s3[['a','e']])
print(s3.loc[l])
c= pd.DataFrame(b)
print(c)
d= pd.DataFrame(c,columns=["Roll No"])
print(d)
d1= pd.DataFrame(b,columns=["Roll No"])
print(d1)
