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
print(type(np.concatenate))

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

#remainders
#Return the remainders

import numpy as np
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([3, 7, 9, 7, 9])

newarr = np.mod(arr1, arr2)

print(newarr)

#Return the remainders

import numpy as np
arr1 = np.array([15, 22, 32, 52, 60])
arr2 = np.array([3, 7, 9, 7, 9])

newarr = np.remainder(arr1, arr2)

print(newarr)

#Quotients and the mod
#Return the quotient and the mod:

import numpy as np
arr1 = np.array([10, 20, 32, 47, 60])
arr2 = np.array([3, 7, 9, 7, 9])

newarr = np.divmod(arr1, arr2)

print(newarr)

#Absolute values

import numpy as np

arr = np.array([-1,-2,-3,0,1,6,3])

newarr = np.absolute(arr)

print(newarr)

#ROunding Decimals

#Truncation
#Truncate elements of following array:

import numpy as np

arr = np.trunc([-3.1666, 3.6667])

print(arr)
#Using fix()
import numpy as np

arr = np.fix([-6.6666, 2.49999])

print(arr)

#Rounding
#Round off 3.1417 to 2 decimal places

import numpy as np
arr = np.around(3.1417, 2)

print(arr)

#Round off 2.5555555 to 3 decimal places

import numpy as np
arr = np.around(2.5555555, 3)

print(arr)

#floor
# Floor the elements of following array:
import numpy as np
arr = np.floor([-3.16667, 3.666667])

print(arr)

#Ceil
# Ceil the elements of following array:
import numpy as np
arr = np.ceil([-3.16667, 3.666667])

print(arr)

#Ufunc logs
#log at base 2
#Find log at base 2 of all elements of following array:

import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))

#log at base 10
#Find log at base 10 of all elements of following array:

import numpy as np

arr = np.arange(1, 10)

print(np.log10(arr))   

#Log at base e
#Find log at base e of all elements of following array:

import numpy as np

arr = np.arange(1, 10)

print(np.log(arr)) 
  
#Log at any base
from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))

#Take a look
from math import log
import numpy as np
nplog = np.frompyfunc(log, 2, 1)

arr = np.array([10, 100, 1000])
bases = np.array([2, 10, 5])

result = nplog(arr, bases)
print(result)'''

#ufunc Summations
#Add the values in arr1 to the values in arr2:
'''
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)
print(newarr)

#Sum the values in arr1 to the values in arr2:

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])
print(newarr)

#Summation over an axis
#Perform summation in the following array over 1st axis:

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis = 1)
print(newarr)

#Cumulative sum

#Perform cumulative summation in the following array:

import numpy as np

arr = np.array([1, 2, 3])

newarr = np.cumsum(arr)

print(newarr)

#ufunc products
#Find the product of the elements of this array:

import numpy as np

arr = np.array([1, 2, 3, 4])
x = np.prod(arr)

print(x)

# Find the product of the elements of two arrays:
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

x = np.prod([arr1, arr2])
print(x)

#Product over an axis
#Perform summation in the following array over 1st axis:
import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

newarr = np.prod([arr1, arr2], axis = 1)

print(newarr)

#Cumulative Product
#Take cumulative product of all elements for following array:
import numpy as np
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)

#ufunc Differences
#Compute discrete difference of the following array:
import numpy as np
arr = np.array([10, 22, 34, 27])
newarr = np.diff(arr)

print(newarr)

#Compute discrete difference of the following array:
import numpy as np
arr = np.array([10, 22, 34, 27])
newarr = np.diff(arr, n=2)

print(newarr)        

#Ufunc  Finding LCM
#Find the LCM of the following two numbers:
import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)

#Find lcm in arrays
#Find the LCM of values of the following array:

import numpy as np
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)

print(x)

#Finding GCD
#FInd the HCF of the following two numbers:
import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1, num2)

print(x)

#Finding GCD in arrays

#Find the GCD for all of the numbers in the following array:
import numpy as np
arr = np.array([20, 8, 32, 36,16])
x = np.gcd.reduce(arr)

print(x)

#ufunc Trigonometric
#Find sine value of PI/2:
import numpy as np
x = np.sin(np.pi/2)
print(x)

# Find sine values for all of the values in arr:
import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)

#Convert all of the values in following array arr to radians:
import numpy as np
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)

#Convert all of the values in following array arr to degrees:
import numpy as np

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)

print(x)

#Finding Angles
#Find the angle of 1.0
import numpy as np
x = np.arcsin(1.0)
print(x)


#Angle of each value in array
#Find the angle for all of the sine values in the array
import numpy as np

arr = np.array([1, -1, 0, 0.1])
x = np.arcsin(arr)

print(x)     

#Hypotenues
 # Find the hypotenuse for 4 base and 3 perpendicular:
import numpy as np

base = 3
perp = 4

x = np.hypot(base, perp)

print(x)

#Hyperbolic functions
#Find sinh value of pi/2:

import numpy as np

x = np.sinh(np.pi/2)

print(x)

# Find cosh values for all of the values in arr:
import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.cosh(arr)

print(x)        

#Finding angles of hyperbolic
#Find the angle of 1.0
import numpy as np

x = np.arcsinh(1.0)

print(x)      

#Find the angle for all of the tanh values in the array
import numpy as np

arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)

print(x)      '''

#ufunc Set Operation

# Convert following array with repeated elements to a set:
import numpy as np 
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5 , 6, 7])

x = np.unique(arr)

print(x)


#Finding union
#Find union of the following two set ARRAYS

import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)


# Find intersection of the following two set arrays:
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])

newarr = np.intersect1d(arr1, arr2)

print(newarr)


#Finding Symmetric Difference
# FInd the symmetric difference of the set1 and set2:

import numpy as np
set1 = np.array([1, 2, 3, 4, 5])
set2 = np.array([3, 4, 5, 6, 7])

newarr = np.setxor1d(set1, set2, assume_unique = True)

print(newarr)