def collatz(number):

    while number != 1:
         if number % 2 == 0:
            number = number // 2
            print(number)
         else:
            number = number * 3 + 1
            print(number)
try:
      collatz(number = int(input("Enter a Number:")))
except ValueError:
    print("Value Error :Invalid Input Type. this is not a number")     
  