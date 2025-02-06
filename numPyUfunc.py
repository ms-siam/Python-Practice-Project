'''#Add the elements of two lists
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i,j in zip(x, y):
	z.append(i + j)
print(z)

#With ufunc, we can use the add() function
import numpy as np
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)

#Create your own ufunc for addition
import numpy as np
def myadd(x, y):
    return x+y
myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([11, 12, 13, 14], [22, 23, 24, 25]))

#Check function type
import numpy as np
print(type(np.add))

# Check the type of another function: concatenate()

import numpy as np
print(type(np.concatenate))'''

#Simple ARITHMETIC

#Addition of arrays
#Add the values in arr1 to the values in arr2:

import numpy as np
arr1 = np.array([10,11,12,13,14,15])  
arr2 = np.array([20,21,22,23,24,25])

newarr = np.add(arr1, arr2)

print(newarr)

#Subtract the values in arr1 to the values in arr2:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr1 = np.subtract(arr1, arr2)

print(newarr1)

#Multiply the values in arr1 with the values in arr2:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr)

#Division
#Divide the values in arr1 with the values in arr2:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)

#Power
#Raise the valules in arr1 to the power of values in arr2:
import numpy as np

arr1 = np.array([10, 2, 3, 4, 5, 6])
arr2 = np.array([3, 5, 6, 8, 2, 3])

newarr = np.power(arr1, arr2)

print(newarr)