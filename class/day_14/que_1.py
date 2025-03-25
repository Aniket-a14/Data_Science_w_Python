import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
#boxplot
plt.figure(figsize=(7, 5))
sns.boxplot(x='species', y='sepal_length', data=iris)
plt.title('Iris Dataset')
plt.show()

#histogram
plt.figure(figsize=(7, 5))
sns.histplot(data=iris, x='sepal_length', kde=True)
plt.title('Iris Dataset')
plt.show()

#heatmap
#plt.figure(figsize=(6, 4))
#sns.heatmap(iris.corr(),annot=True, cmap='coolwarm')
#plt.title('Iris Dataset')
#plt.show()
plt.figure(figsize=(10,6))
sns.heatmap(iris.corr(numeric_only=True),annot=True, cmap='coolwarm')
plt.show()

#scatterplot
plt.figure(figsize=(7, 5))
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='species', style='species', palette='deep')
plt.title('Iris Dataset')
plt.show()

