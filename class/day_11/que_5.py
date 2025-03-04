import matplotlib.pyplot as plt

labels = ["Apple", "Banana", "Cherry", "Dates", "Elderberry", "Fig", "Grape", "Honeydew", "Indian Plum", "Jackfruit"]

sizes = [15, 10, 15, 10, 20, 25, 30, 35, 40, 45]

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'cyan', 'magenta', 'lightgreen']


plt.pie(sizes, labels=labels,colors=colors, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
# What is the purpose of the autopct parameter in the pie chart?
#The autopct parameter in a pie chart in Python's matplotlib library is used to format the value displayed on each wedge of the pie chart. It is a string that is used to format the percentage value of each wedge. The percentage value is computed by dividing the value of the wedge by the sum of all values and multiplying by 100. The autopct parameter can be used to display the percentage value with a specific number of decimal places or with a specific format. For example, autopct='%1.1f%%' will display the percentage value with one decimal place. The default value of autopct is None, which means that no percentage value will be displayed on the pie chart.
