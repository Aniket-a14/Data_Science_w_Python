import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line 1')

'''
'o' - Circle
'v' - Triangle Down
'^' - Triangle Up
'<' - Triangle Left
'>' - Triangle Right
's' - Square
'*' - Star
'+' - Plus
'x' - Cross
'p' - Pentagon
'h' - Hexagon
'D' - Diamond
'd' - Thin Diamond
'P' - Plus (filled)
'X' - Cross (filled)
_ - Horizontal Line
'.' - Point
'''

plt.xlabel('Number')
plt.ylabel('Value')
plt.title('Basic Number Plot')

plt.legend()
plt.show()
