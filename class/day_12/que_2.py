import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame({'Sales': [10000, 15000, 12000], 'Profit': [4390, 6720, 6010]}, index=['Furniture', 'Technology', 'Office Supplies'])

plt.figure(figsize=(6,4))
corr = data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

