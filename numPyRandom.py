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