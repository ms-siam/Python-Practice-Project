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

NestedList = [[1,2,3], [4,5,6], [7,8,9]]

FlattenList = [digit for row in NestedList for digit in row]
print(FlattenList)

#Problem 4: Dictionary Comprehension
#Create a dictionary where keys are numbers 1-5 and values are their cubes.

dict = {num: num**3 for num in range(1,6)}

print(dict)


#Problem 5: Complex Filtering
#Given words = ["python", "is", "awesome", "and", "powerful"] , create a list of tuples containing (word, length)

words = ["python", "is", "awesome", "and", "powerful"]

list = [(w, len(w)) for w in words]
print(list)

#Problem 6: Conditional Expression
#Create a list comprehension that converts temperatures from Celsius to Fahrenheit, but only for
#temperatures above 0°C. Input: celsius_temps = [-10, 0, 15, 25, 30, -5]

celsius_temps = [-10, 0, 15, 25, 30, -5]

farenheits_temp = [temp * (9/5) + 32 for temp in celsius_temps if temp > 0]
print(farenheits_temp)

#Problem 7: Set Comprehension Challenge
#From a string "hello world programming", create a set of unique consonants (non-vowel letters).

consonant = { letter for letter in "hello world programming" if letter not in ('aeiou ') }
print(consonant)

#Problem 8: Higher-Order Function
#Write a function apply_operation(func, numbers) that takes a function and a list of numbers, applies the function to each number, and returns the results.

def apply_operation(func, numbers):
    return [func(num) for num in numbers]

squares = apply_operation(lambda x: x**2, [2, 8, 1, 0])
print(squares)
'''
Problem 9: Flexible Arguments
Create a function calculate(*args, **kwargs) that:
•⁠  ⁠Accepts any number of numbers as positional arguments
•⁠  ⁠Accepts an operation keyword argument ('sum', 'multiply', 'max', 'min')
•⁠  ⁠Returns the result of the operation on the numbers
'''


'''
Problem 10: Closure Implementation
Write a function factor.
create_multiplier(factor) that returns a function which multiplies its input by the given
'''

'''
Problem 12: Generator Function
Create a generator function prime_generator(limit) that yields prime numbers up to the given limit.
'''


'''
Problem 14: Basic Class Design
Create a Rectangle class with:
•	Constructor that takes width and height
•	Methods: area() , perimeter() , is_square()
•	String representation showing dimensions
'''

class rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        self.area = self.height * self.width
        print(f'Area of a rectangle containg {self.height} height and {self.width} width is {self.area}.')

    def perimeter(self):
        self.perimeter = 2 * (self.height + self.width)
        print(f'Perimeter of a rectangle containg {self.height} height and {self.width} width is {self.perimeter}.')

    def is_square(self):
        print(f'This rectangle is square: {self.height == self.width}')

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

Box= rectangle(10, 5)
print(Box)
Box.is_square()
Box.perimeter()


'''
Problem 15: Class with Validation Create a Temperature class that:
•	Stores temperature in Celsius
•	Has methods to convert to Fahrenheit and Kelvin
•	Validates that temperature is above absolute zero (-273.15°C)
•	Raises appropriate exceptions for invalid temperatures
'''

