import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("class/day_15/Sales.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

print(df.corr(numeric_only=True))
print(df.cov(numeric_only=True))

plt.figure(figsize=(6,4))
plt.hist([df["Sales_Cost"], df["Sales_Amt"], df["Sales_Qty"]], bins=10, label=["Sales_Cost", "Sales_Amt", "Sales_Qty"])
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

plt.figure(figsize=(10,5))
sns.heatmap(df.corr(numeric_only=True),annot=True)
plt.title("HeatMap")
plt.show()

sns.scatterplot(data=df,x="Sales_Cost",y="Sales_Amt",hue="SalesType",style="SalesType")
plt.title("Sales_Cost vs Sales_Amt")
plt.show()

sns.pairplot(data=df.select_dtypes(include=["number"]))
plt.title("PairPlot")
plt.show()
