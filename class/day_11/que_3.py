import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,4,2,5,4,2,5,7,4,3,6,9,6,3,6,8,3,2,7,6]
y = [10,20,25,30,40,50,60,70,80,90,100,110,54,2,4,56,57,23,45,67,78,89,90,23,45,67,89,90,23]

plt.scatter(x, y, marker='o', color='lightblue', label='Scatter 1')
plt.xlabel('Number')
plt.ylabel('Value')
plt.title('Basic Number Plot')
plt.legend()
plt.show()