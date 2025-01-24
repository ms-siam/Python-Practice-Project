
while True:
    print('What is your name?')
    name = input()
    if name != 'Siam':
        continue                            # Jump into First line of while loop
    print('Hello, Siam. What is the password? (It  is a fish)')
    password = input()
    if password == 'Swordfish':
        break
print('Access Granted')

