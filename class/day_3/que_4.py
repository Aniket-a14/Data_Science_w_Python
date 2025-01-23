import numpy as np #creation of an array

a= np.array([1,2,3,4]) #creating a 1D array
print("Array is:", a)


b= np.arange(6).reshape(2,3) #creating a 2D array
print("Array is:", b)


a= np.matrix('1 2; 3 4') #string input
print("Via string input : \n", a, "\n\n")


b= np.matrix([[5,6,7], [4,6]]) #array-like input
print("Via array-like input : \n", b)