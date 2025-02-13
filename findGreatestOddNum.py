#! python3
# findGreatestOddNum.py- Find the highest odd number in a given integer

num = input('Type an number: ')
index = 0
for i in range(len(num)-1,-1,-1):
    if int(num[i]) % 2 == 1:
        index = i
        break 
    
index = i + 1
oddNum = num[:index]

