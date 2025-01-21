def isPhoneNumber(text):
    if len(text) == 16 and text[0] == '+' and text[4] == ' ' and text[9] == '-' and text[1:4].isdecimal() and text[5:9].isdecimal() and text[10:].isdecimal():
        return True
    return False
Num = '+880 1521-768750'
print(f"Is {Num} a BD Phone number? {isPhoneNumber(Num)} ")
