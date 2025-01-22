import re

PassSyntax = re.compile(r'''(
                        (?=.*[A-Z])(?=.*[a-z])(?=.*\d)
                        (?=.*[!@#$%^&*()-_=+{};:'",.<>?/~|]).{8,})
                        ''', re.VERBOSE)
password = input("Enter your password: ")

matchPass = PassSyntax.search(password)

if matchPass:
    print("Password is strong")
else:
    print("Password is weak")