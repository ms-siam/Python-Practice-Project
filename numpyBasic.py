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

arr = np.array([1,2,3,4,5])  

x = arr.copy()                  #coping and assigning the array to x
arr[0] =42                     #changing an element of arr
print(arr)                      #Output:[42  2  3  4  5]
print(x)                        #Output:[1 2 3 4 5]

y = arr.view()                  #viewing and storing the array to y
arr[0] = 42                     #changing an element of arr
print(arr)                      #Output:[42  2  3  4  5]
print(y)                        #Output:[42  2  3  4  5]

z = arr.view()  
z[0] = 31  
  
print(arr)                     #Output:[31  2  3  4  5]
print(z)                       #Output:[31  2  3  4  5]

arrs = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arrs.shape)

arrs5 = np.array([1, 2, 3, 4], ndmin=5)

print(arrs5)
print('shape of array :', arrs5.shape)

#Reshaping arrays
arrRs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arrRs.reshape(4, 3)
print(newarr)

arrRs3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr3 = arrRs3.reshape(2, 3, 2)

print(newarr3)


#Check if the returned array is a copy or a view

arrC = np.array([1, 2,3,4,5,6,7,8])  
  
print(arrC.reshape(2, 4).base) 

#Convert 1D array with 8 elements to 3D array with 2x2 elements:
arrUd = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarrUd = arrUd.reshape(2, 2, -1)

print(newarrUd)

#Flattening the arrays
arrF = np.array([[1, 2, 3], [4, 5, 6]])

newarrF = arrF.reshape(-1)

print(newarrF)

#iterating the arrays

arrI = np.array([1, 2, 3])  
for x in arrI:
    print(x )
    
arrII = np.array([[1, 2, 3], [4, 5, 6]])

for x in arrII:
  print(x, end=', ')
  
  
arrIII = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arrIII:
  print(x)
  
  
arrIe2 = np.array([[1, 2, 3], [4, 5, 6]])

for x in arrIe2:
  for y in x:
    print(y)
    
    
arrIe3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arrIe3:
  for y in x:
    for z in y:
      print(z)
      
#Iterate through the following 3-D array:      
arr3ni = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr3ni):
  print(x, end=' ')
  
  
arrnb = np.array([1, 2, 3])

for x in np.nditer(arrnb, flags=['buffered'], op_dtypes=['S']):
  print(x)

arrds = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arrds[:, ::2]):
  print(x)
  
arrNe = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arrNe):
  print(idx, x)
  
arrNe2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arrNe2):
  print(idx, x)
  
  
arr1j = np.array([1, 2, 3])

arr2j = np.array([4, 5, 6])

arrj = np.concatenate((arr1j, arr2j))

print(arrj)

arr1jr = np.array([[1, 2], [3, 4]])

arr2jr = np.array([[5, 6], [7, 8]])

arrjr = np.concatenate((arr1jr, arr2jr), axis=1)

print(arrjr)

arr1s = np.array([1, 2, 3])

arr2s = np.array([4, 5, 6])

arrs = np.stack((arr1s, arr2s), axis=1)

print(arrs)