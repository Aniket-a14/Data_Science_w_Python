import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

colors = list(mcolors.CSS4_COLORS.keys())
print(colors)

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 37, 24]

plt.bar(categories, values, color='lightblue', label='Bar 1')

plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Basic Category Plot')

plt.legend()
plt.show()
