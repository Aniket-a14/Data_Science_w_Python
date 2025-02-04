import numpy as np
'''
You are working as a data analyst for a company that deals with large datasets. Your team receives a 2D NumPy array containing customer transaction data, where each row represents a different customer, and columns represent transactions amounts in different months.

Using Numpy functions:
    1. Find the maximum, minimum, and total transaction amount across all customers
    2. Compute the cumulative sum of transactions column wise
    3. Flatten the 2D array into a 1D array and sort the transactions in ascending order
    4. Transform the dataset by reshaping it into a different structure

Write a python code to achieve these tasks and explain the significance of each function in data transformation

#sample transaction data(4 customers, 5 months) 
'''


a= np.random.randint(20,500,(4,5))
b= np.max(a)
c= np.min(a)
d= np.sum(a)

print("Random customer data for 5 months:\n",a)
print("Maximun transaction amount: ",b)
print("Minimum transaction amount: ",c)
print("Sum of all transaction data: ",d)


e= np.cumsum(a)
print("Cummulative sum of data:\n",e)


f= a.flatten()
# f= np.sort(a.flatten())   if you want to sort the data
print("Data after flattening:\n",f)

g= a.transpose()
print("Transpose of the data:\n",g)

h= a.reshape(5,4)
print("Reshaping the matrix:\n",h)
