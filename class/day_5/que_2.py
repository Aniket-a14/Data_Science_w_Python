import numpy as np


print("Reference Variable")
a=np.arange(1,7).reshape(2,3)
b=a
print("Array is:\n",a)
print("Array is:\n",b)
print(a is b)
print(b is a)



print("Shallow Copy")
c=a.view()
print("Array is:\n",a)
print("Array is:\n",c)
print(a is c)
print(c is a)
c[0][1]=22
print("Array is:\n",a)
print("Array is:\n",c)



print("Deep Copy")
d=a.copy()
print("Array is:\n",a)
print("Array is:\n",d)
print(a is d)
print(d is a)
d[0][1]=33
print("Array is:\n",a)
print("Array is:\n",d)