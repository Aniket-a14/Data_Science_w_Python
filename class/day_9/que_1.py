import pandas as pd
import numpy as np

data = pd.read_csv("class/day_8/tips.csv")

df = pd.DataFrame(data)

sorted_df = df.sort_values(by='total_bill', ascending=False)
print("Sorted Values:\n", sorted_df, "\n")

pivot_table = df.pivot_table(values='total_bill', index='day', columns='Gender', aggfunc='sum')
print("Pivot table:\n", pivot_table, "\n")

filtered_df = df.loc[df['total_bill']>20]
print("Filtered data (Total Bill > 20):\n", filtered_df.head(), "\n")

print("First 5 rows using iloc:\n", df.iloc[0:5], "\n")

df_renamed = df.rename(columns={'total_bill': 'Total_bill_amount'})
print("Renamed Columns names:\n", df_renamed.columns, "\n")

print(df)

record = np.array([20.12,4.0, 'Male', 'Yes', 'Mon', 'Dinner', '2.0'])
df.loc[len(df)] = record
#df = df.sort_index().reset_index(drop=True)
print(df)
