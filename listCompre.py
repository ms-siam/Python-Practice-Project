# problem 1: Basic Transformations
#Create a list of squares for numbers 1-10 using list comprehension.

square = [sq**2 for sq in range(1,11)]
print(square)

#Problem 2: Filtering with Conditions
#Create a list of even numbers from 0-20 that are also divisible by 4.

numbers= []

for i in range(21):
    numbers.append(i)

CondEven = [even for even in numbers if even>0 and even%4 == 0]

print(CondEven)

#Problem 3: Nested Structure Flattening
#Flatten this 2D matrix using list comprehension: [[1,2,3], [4,5,6], [7,8,9]] Expected output: [1,2,3,4,5,6,7,8,9]
