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
plt.hist(data=df,x=["Sales_Cost","Sales_Amt","Sales_Qty","SalesType"],bins=10)
plt.title("Histogram")
plt.show()

plt.figure(figsize=(10,5))
sns.heatmap(df.corr(numeric_only=True),annot=True)
plt.title("HeatMap")
plt.show()

sns.scatterplot(data=df,x="Sales_Cost",y="Sales_Amt",hue="SalesType",style="SalesType")
plt.title("Sales_Cost vs Sales_Amt")
plt.show()

sns.pairplot(data=df,hue="SalesType",palette="husl",markers=["o","D"])
plt.title("PairPlot")
plt.show()
