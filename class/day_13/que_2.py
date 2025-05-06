import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris = sns.load_dataset('iris')

data = pd.DataFrame(iris)
print(data.describe())


plt.figure(figsize=(7, 5))
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='species', style='species', palette='deep')
plt.title('Iris Dataset')
plt.show()

plt.figure(figsize=(7, 5))
sns.lineplot(x='sepal_length', y='sepal_width', data=iris, hue='species', style='species', palette='deep', marker='o')
plt.title('Iris Dataset')
plt.show()