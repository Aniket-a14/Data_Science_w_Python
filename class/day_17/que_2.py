import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


data = sns.load_dataset('iris')
print(data.describe())

mean_i = data['sepal_length'].mean()
std_i = data['sepal_length'].std(ddof=1)

z_score = (data['sepal_length']-mean_i)/std_i
outliers = data[np.abs(z_score)>3]
print(outliers)