import numpy as np

a = np.array([1,2,3,4])
print("Array is:\n",a)

b= np.array([[1,2,3],[4,5,6]])
print("Array is:\n",b)

c= np.array([[[1,2,3],[9,3,7]],[[4,5,6],[7,8,9]]])
print("Array is:\n",c)

d= np.eye(2,3)
print("Array is:\n",d)

e= np.full([2,3],10)
print("Array is:\n",e)

print("Cummulative sum column wise:\n",b.cumsum(axis=0))
print("Cummulative sum row wise:\n",b.cumsum(axis=1))
print("Flatten function:\n",b.flatten())
print("Transpose function:\n",b.transpose())