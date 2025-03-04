import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)
plt.hist(data, bins=100, alpha=0.5, color='forestgreen', edgecolor='black')
'''
The bins parameter specifies the number of bins in the histogram. Bins can be a single number or a list of numbers.
If bins is an integer, it defines the number of equal-width bins in the range.
'''
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()