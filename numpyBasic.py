import numpy as np
arr = np.array([12, 11, 12, 10, 12, 15, 122, 19, 20, 21, 31])
print(arr[1:5:2])
arr1 = np.array((1, 2, 3, 12, 23))
print(arr1)
d0arr = np.array(42)

print(d0arr)

r = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(r.ndim)

f = np.array([1, 2, 3], ndmin=5)
print(f.ndim)

print(arr[2] + arr[3])

arr3 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr3[1, -1])

arr6 = np.array(['apple', 'banana', 'cherry'])

print(arr6.dtype)