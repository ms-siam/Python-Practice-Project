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

print(myadd([11, 12, 13, 14], [22, 23, 24, 25]))'''

#Check function type
import numpy as np
print(type(np.add))

# Check the type of another function: concatenate()

import numpy as np
print(type(np.concatenate()))