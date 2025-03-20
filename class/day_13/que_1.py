import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("class/day_12/samplesuperstore.csv")
print(data.head())
sns.set_theme(style="whitegrid")

# Line plot for total sales over time
plt.figure(figsize=(10, 5))
data['Order Date'] = pd.to_datetime(data['Order Date'])
sns.lineplot(x='Order Date', y='Sales', data=data)
plt.title('Total Sales Over Time')
plt.xlabel('Order Date')
plt.ylabel('Total Sales')
plt.show()

# Bar plot for total profit by category
plt.figure(figsize=(8, 5))
barplot = sns.barplot(x='Category', y='Profit', data=data,errorbar=None)
plt.title('Total Profit by Category')
plt.xlabel('Category')
plt.ylabel('Total Profit')
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.2f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')    
plt.show()
'''
barplot.patches iterate over each bar in the plot
annotate() function is used to add text to the plot
format() function is used to format the text to 2 decimal places
get_height() function is used to get the height of the bar
get_x() function is used to get the x-coordinate of the bar
get_width() function is used to get the width of the bar
'''

# Scatter plot for Sales vs profit
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Sales', y='Profit', data=data, hue="Ship Mode", style="Ship Mode", s=100)
plt.title('Sales vs Profit by Ship Mode')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()

# Heatmap for correlation between numerical columns
plt.figure(figsize=(6, 4))
corr = data[['Sales', 'Quantity', 'Discount', 'Profit']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()