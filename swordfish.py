while True:
    print('What is your name?')
    name = input()
    if name != 'Siam':
        continue
    print('Hello, Siam. What is the password? (It  is a fish)')
    password = input()
    if password == 'Swordfish':
        break
print('Access Granted')
