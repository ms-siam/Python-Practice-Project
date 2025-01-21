def isPhoneNumber(text):
    if len(text) == 16 and text[0] == '+' and text[4] == ' ' and text[9] == '-':
        print('Yes')
Num = '+880 1521-768750'
print(f"Is {Num} a BD Phone number?")
isPhoneNumber(Num)