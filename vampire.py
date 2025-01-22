print('What is ur name ?')
name = input()
print('What is ur age ?')
age = input()
if name == 'Alice':
    print('Hi, Alice') #if inputted name is Alice thr code will ignore rest of the lines after printing this line.
elif age < '12': # here i need to cover the 12 with inverted comma bcz age variable was inputted and the input function always makes a value stings so i also need to make the 12 a string
    print('You are not alice, kiddo') #if inputted name is not alice then the code will run this line accordingly . and the inputted age goes right with any of this elif conditions , program will run that line and ignore rest of them.
elif age > '2000':
    print('Unlike u , alice is not an undead, immortal vampire')
elif age > '100':
    print(' u r not alice, grannie')

#This is another code for same result.
name = 'carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not alice, kiddo')
elif age > 2000:
    print('Unlike u , alice is not an undead, immortal vampire')
elif age > 100:
    print(' u r not alice, grannie')
