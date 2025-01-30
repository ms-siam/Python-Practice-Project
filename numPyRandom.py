#Generate a random integer from 0 to 100
from numpy import random

x = random.randint(100)

print(x)

#Generate Random Float
xf = random.rand()

print(xf)

#Generate a 1-D array containing 5 random integers from 0 to 100:
xia=random.randint(100, size=(5))

print(xia)

#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
xia2 = random.randint(100, size=(3, 5))

print(xia2)