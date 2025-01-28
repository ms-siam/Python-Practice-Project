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
arrh = np.hstack((arr1s, arr2s))#np.hstack stacks arrays horizontally (into a single 1D array).

print(arrh)

arrv = np.vstack((arr1s, arr2s))#np.vstack stacks arrays vertically (row-wise).

print(arrv)

arrhd = np.dstack((arr1s, arr2s))

print(arrhd)

arrSp = np.array([1, 2, 3, 4, 5, 6])

newarrSp = np.array_split(arrSp, 3)

print(newarrSp)

arrSp1 = np.array([1, 2, 3, 4, 5, 6])

newarrSp1 = np.array_split(arrSp1, 4)

print(newarrSp1)

#Access the splitted arrays
arrSp2 = np.array([1, 2, 3, 4, 5, 6])

newarrSp2 = np.array_split(arrSp2, 3)

print(newarrSp2[0])
print(newarrSp2[1])
print(newarrSp2[2])

#Split the 2-D array into three 2-D arrays.

arrSp3 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarrSp3 = np.array_split(arrSp3, 3)

print(newarrSp3)

arrSp4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarrSp4 = np.array_split(arrSp4, 3)

print(newarrSp4)

#Split the 2-D array into three 2-D arrays along columns
arrSx1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarrSx1 = np.array_split(arrSx1, 3, axis=1)

print(newarrSx1, end='\n')

arrhsp = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarrhsp = np.hsplit(arrhsp, 3)

print(newarrhsp)

#Find the indexes where the value is 4:
arrw = np.array([1, 2, 3, 4, 5, 4, 4])

xw = np.where(arrw == 4)

print(xw)

#Find the indexes where the values are even:

arrwe = np.array([1, 2, 3, 4, 5, 6, 7, 8])

xwe = np.where(arrwe%2 == 0)

print(xwe)

#Find the indexes where the value 7 should be inserted:
arrss7 = np.array([6, 7, 8, 9])

xss7 = np.searchsorted(arrss7, 7)

print(xss7)

#Find the indexes where the values 2, 4, and 6 should be inserted

arrMss = np.array([1, 3, 5, 7])

xMss = np.searchsorted(arrMss, [2, 4, 6])

print(xMss)

#Sort the array:
arrSort = np.array([3, 2, 0, 1])

print(np.sort(arrSort))

#sort arrays of strings, or any other data type:
arrSs = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arrSs))

arrSb = np.array([True, False, True])

print(np.sort(arrSb))
#sorting a 2-D array
arrs2d = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arrs2d))

#Create an array from the elements on index 0 and 2:
arrfa = np.array([41, 42, 43, 44])

xfa = [True, False, True, False]

newarrfa = arrfa[xfa]

print(newarrfa)

#Create a filter array that will return only values higher than 42
arrcfa = np.array([41, 42, 43, 44])

# Create an empty list
filter_arrcfa = []

# go through each element in arr
for element in arrcfa:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arrcfa.append(True)
  else:
    filter_arrcfa.append(False)

newarrcfa = arrcfa[filter_arrcfa]

print(filter_arrcfa)
print(newarrcfa)

arrfcap = np.array([41, 42, 43, 44])

filter_arrfcap = arrfcap > 42

newarrfcp = arr[filter_arrfcp]

print(filter_arrfcp)
print(newarr)