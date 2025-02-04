import numpy as np

# l=[]
# n= int(input("Enter number of elements "))

# for i in range(0,n):
#     l.append(int(input("Enter value ")))

# a= np.array(l)
# print("View from last: ",a[::-1])
# print("View as normal: ",a)


a= np.array(([1,2,3],[4,5,6],[1,2,3]))
b= np.array(([1,2,3],[4,5,6],[1,2,3]))
d= np.zeros([3,3],dtype=int)
s=0

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            d[i][j] += a[i][k] * b[k][j]

print("Matrix multiplication using for loop:\n",d)
print("Matrix multiplication with dot operator:\n",a.dot(b))
print("Matrix multiplication with @ operator:\n",a@b)
print(d==a.dot(b))