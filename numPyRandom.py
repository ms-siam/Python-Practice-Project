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

#Generate a 1-D array containing 5 random floats:
xfa = random.rand(5)

print(xfa)

#Generate a 2-D array with 3 rows, each row containing 5 random numbers:
xfa2 = random.rand(3, 5)
print(xfa2)

#Return one of the values in an array:
xrva = random.choice([3, 5, 7, 9])

print(xrva)

#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
xrva2 = random.choice([3, 5, 7, 9], size=(3, 5))

print(xrva2)