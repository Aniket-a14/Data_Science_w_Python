import numpy as np
import matplotlib.pyplot as plt

data = np.array([10,12,14,15,18,21,22,25,28,2,-10,30])

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3-Q1

lower_bound = Q1 - 1.5 * IQR
print("Lower Bound:",lower_bound)
upper_bound = Q3 + 1.5 * IQR
print("Upper Bound:",upper_bound)
outliers_iqr = data[(data<lower_bound) | (data>upper_bound)]

print("Outliers are:",outliers_iqr)

plt.figure(figsize=(6,4))
plt.boxplot(data,vert=False)
plt.xlabel("Values")
plt.title("Boxplot to show outliers")
plt.show()


#Calculate Z-score
Z = (data-np.mean(data))/np.std(data,ddof=1)    #np.sqrt(np.mean(data**2)-(np.mean(data))**2)
outliers = data[np.abs(Z)>2]
print("Outliers based on Z-score:",outliers)

