import pandas as pd

df = pd.read_csv("./class/day_8/tips.csv")
# df['sum'] = df['total_bill'] + df['tip']
# print(df,"\n")

print("Data sucessfully Loaded\n")
print("First 10 rows of the data:", df.head(10),"\n")
print("Last 5 rows of the data:", df.tail(5),"\n")
print("Information about the data:", df.info(),"\n")
print("Description of the data:", df.describe(),"\n")
print("Shape of the data:", df.shape,"\n")
print("Columns of the data:", df.columns,"\n")
print("Index of the data:", df.index,"\n")
print("Data types of the data:", df.dtypes,"\n")
print("Value counts of the data:", df.value_counts(),"\n")
print("Missing values in the data:", df.isnull().sum(),"\n")
print("Dropping missing values:", df.dropna(),"\n")

