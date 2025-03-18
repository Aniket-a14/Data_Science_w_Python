import seaborn as sns
import matplotlib.pyplot as plt

categories = ['Furniture', 'Technology', 'Office Supplies']
profit = [4390, 6720, 6010]
sales = [10000, 15000, 12000]

sns.set_theme(style="whitegrid")
plt.figure(figsize=(8,5))
sns.lineplot(x=categories, y=sales, label='Sales', marker='o')
plt.title('Sales Trend by Category')
plt.xlabel('Category')
plt.show()

plt.figure(figsize=(8,5))
barplot = sns.barplot(x=categories, y=profit, palette='viridis', errorbar=None)
plt.title('Profit by Category')
for i,value in enumerate(profit):
    barplot.text(i, value + 100, f'[value:.2f]', ha = 'center')
    
plt.show()


plt.figure(figsize=(8,5))
sns.scatterplot(x=sales, y=profit, hue=categories, s=100)
plt.title('Profit vs Sales')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()

