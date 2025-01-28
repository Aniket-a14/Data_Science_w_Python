import numpy as np

# Define two arrays
array1 = np.array([[1, 2, 3, 4], [7, 3, 8, 9]])
array2 = np.array([[9, 1, 6, 8], [5, 7, 2, 4]])

# Perform element-wise operations
print("Subtraction:\n", array1 - array2)
print("Addition:\n", array1 + array2)
print("Multiplication:\n", array1 * array2)
print("Division:\n", array1 / array2)

# Reshape and print arrays
array1 = np.arange(6).reshape(2, 3)
print("Array is:\n", array1)
array2 = np.arange(10, 22, 2).reshape(3, 2)
print("Array dimensions:", array2.ndim)

# Perform matrix multiplication
print("Matrix multiplication (using @):\n", array2 @ array1)
print("Matrix multiplication (using dot):\n", array2.dot(array1))