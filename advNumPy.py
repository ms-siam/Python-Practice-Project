# Broadcasting- 
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
#Setting a value with index range(broadcasting)
arr[0:5] = 10
print(arr)

arr = np.arange(0,11)
print(arr)


sliceOfArr = arr[6:11]
print(sliceOfArr)
