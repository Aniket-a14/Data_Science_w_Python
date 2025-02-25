import pandas as pd
import numpy as np

data = {
    'ID': [1,2,3,4,5],
    'Name': ['Aniket', 'Raj', 'Sayak', 'David', np.nan],
    'Age': [23,np.nan, 45,3,56],
    'City': ['New York', 'Los Angeles', 'Chicago', np.nan, np.nan],
    'Salary': [60000,454444,566556,54545,np.nan]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull().sum())

df_dropped = df.dropna()
print(df_dropped)

df_dropped_columns = df.dropna(axis=1)
print(df_dropped_columns)

df_filled = df.fillna({'Age': df['Age'].mean(), 'City': "Unknown", 'Salary': df['Salary'].median()})
print(df_filled)

df_ffill = df.ffill()
print(df_ffill)

df_bfill = df.bfill()
print(df_bfill)

df_numeric = df.select_dtypes(include=[np.number])
print(df_numeric)

df_interpolate = df_numeric.interpolate()
df_final = df.copy()

df_final[df_numeric.columns]= df_interpolate
print(df_final)